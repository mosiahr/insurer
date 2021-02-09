import csv
import re
import datetime
from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone as django_timezone
from django.core.exceptions import ObjectDoesNotExist

from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

from customer_service.utils import generation_uuid, get_uuid_for_sms
from insurer.settings import DEFAULT_COUNTRY_UA, MEDIA_ROOT, \
    DATE_INPUT_FORMAT_UA
from insurer.conf import FROM_, TO

User = get_user_model()


# class CompanyDirectorate(models.Model):
#     pass
#
#
# class CompanyBranch(models.Model):
#     pass

class MainAbstractModel(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=django_timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(MainAbstractModel):
    INSURANCE_TYPE_CHOICES = [
        ('Ф', _('Individual entity')),
        ('Ю', _('Legal entity')),
    ]

    name = models.CharField(max_length=200)
    ind_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name=_('Individual identification number'))
    address = models.TextField()
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    customer_type = models.CharField(
        max_length=1,
        choices=INSURANCE_TYPE_CHOICES,
        default='Ф')

    def __str__(self):
        return self.name


class Car(MainAbstractModel):
    mark = models.CharField(max_length=50, verbose_name=_('Mark'))
    model = models.CharField(max_length=50, verbose_name=_('Model'))
    registration_place = models.CharField(
        max_length=50, verbose_name=_('Registration Place'))
    registration_country = models.CharField(max_length=50)
    registration_number = models.CharField(
        max_length=50, verbose_name=_('Registration Number'))
    vin_code = models.CharField(max_length=17, verbose_name=_('VIN code'))

    def __str__(self):
        return f'{self.mark} {self.model} ({self.registration_number})'


class IntegerRangeField(models.PositiveSmallIntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None,
                 max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.PositiveSmallIntegerField.__init__(self,
                                                  verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class InsurancePolicy(MainAbstractModel):
    number = models.CharField(max_length=20, verbose_name=_('Policy number'))
    sticker = models.CharField(max_length=20, blank=True, null=True)
    registration_date = models.DateField(verbose_name=_('Registration date'))
    begin_date = models.DateField(verbose_name=_('Begin date'))
    end_date = models.DateField(verbose_name=_('End date'))

    insurance_code = IntegerRangeField(min_value=100, max_value=500)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,
                                 verbose_name=_('Customer'))
    car = models.ForeignKey(Car, on_delete=models.PROTECT,
                            verbose_name=_('Car'))

    sum_insured = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                verbose_name=_('Price'))

    bonus = models.CharField(max_length=1, blank=True, null=True)

    territory = models.TextField()

    is_reinsured = models.BooleanField(
        default=False, verbose_name=_('Insured'))
    is_reinsured_another_company = models.BooleanField(
        default=False, verbose_name=_('Insured in another company'))
    is_impossible_to_call = models.BooleanField(
        default=False, verbose_name=_('Impossible to call'))
    is_called_will_insure = models.BooleanField(
        default=False, verbose_name=_('Was called and will insure'))
    is_called_will_not_insure = models.BooleanField(
        default=False, verbose_name=_('Was called and will not insure'))

    class Meta:
        verbose_name = _('Insurance Policy')
        verbose_name_plural = _('Insurance Polices')

    def __str__(self):
        return self.number

    def count_sms(self) -> int:
        """ Return a quantity of SMS that sent to customer
         about the insurance policy """
        sms_list = MessageSmsInsurancePolicyExpires.objects.filter(
            insurance_policy=self.id)
        return len(sms_list)


class DataFile(MainAbstractModel):
    date_format = DATE_INPUT_FORMAT_UA
    file = models.FileField(upload_to='data_file/%Y/%m/%d')

    class Meta:
        verbose_name = _('Data File')
        verbose_name_plural = _('Data Files')

    def __str__(self):
        return f'{self.file}'

    def get_full_path_file(self):
        return f'{MEDIA_ROOT}/{self.file}'

    @staticmethod
    def parse_date(value, date_format):
        return datetime.datetime.strptime(value, date_format).date()

    @staticmethod
    def parse_number(value):
        return Decimal(re.sub(r',', '.', value))

    def save(self, *args, **kwargs):
        super(DataFile, self).save(*args, **kwargs)
        file = self.get_full_path_file()
        with open(file, 'r') as f:
            reader = csv.reader(f)

            # Skipping unnecessary lines in the file
            for row in reader:
                if row and re.match(r'Textbox3', row[0]):
                    is_mark = True
                    break

            if is_mark:
                for row in reader:
                    if len(row):

                        try:
                            customer = Customer.objects.get(
                                ind_number=row[13])
                        except ObjectDoesNotExist:
                            customer = Customer(
                                # user=self.user,
                                name=row[12],
                                ind_number=row[13],
                                address=row[14],
                                country=row[15],
                                phone=row[16],
                                customer_type=row[17]
                            )
                            customer.save()

                        try:
                            car = Car.objects.get(
                                registration_number=row[22],
                                vin_code=row[23])
                        except ObjectDoesNotExist:
                            car = Car(
                                # user=self.user,
                                mark=row[18], model=row[19],
                                registration_place=row[20],
                                registration_country=row[21],
                                registration_number=row[22], vin_code=row[23]
                            )
                            car.save()

                        try:
                            InsurancePolicy.objects.get(number=row[6])
                        except ObjectDoesNotExist:
                            policy = InsurancePolicy(
                                # user=self.user,
                                number=row[6], sticker=row[7],
                                registration_date=self.parse_date(row[8],
                                                                  self.date_format),
                                begin_date=self.parse_date(row[9],
                                                           self.date_format),
                                end_date=self.parse_date(row[10],
                                                         self.date_format),
                                insurance_code=row[11],
                                customer=customer,
                                car=car,
                                sum_insured=self.parse_number(row[24]),
                                price=self.parse_number(row[25]),
                                bonus=row[26],
                                territory=row[27],
                            )
                            policy.save()


# MESSAGES
class MessageAbstractModel(MainAbstractModel):
    sid = models.CharField(max_length=50, unique=True,
                           default=get_uuid_for_sms)
    body = models.TextField(verbose_name=_('Message body'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.sid


# MESSAGES-SMS
class MessageSmsAbstractModel(MessageAbstractModel):
    from_phone_number = PhoneNumberField(region='US', default=FROM_)
    to_phone_number = PhoneNumberField(region='UA', default=TO)

    class Meta:
        abstract = True
        verbose_name = _('SMS messages')
        verbose_name_plural = _('SMS messages')
        ordering = ['-created']


class MessageSmsInsurancePolicyExpires(MessageSmsAbstractModel):
    insurance_policy = models.ForeignKey(InsurancePolicy,
                                         on_delete=models.PROTECT,
                                         verbose_name=_('Insurance Policy'))
