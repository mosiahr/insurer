import csv
import datetime
import re
from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


from django_countries.fields import CountryField

from insurer.settings import DEFAULT_COUNTRY_OF_CAR_REGISTRATION, MEDIA_ROOT,\
    DATE_INPUT_FORMATS


# class CompanyDirectorate(models.Model):
#     pass
#
#
# class CompanyBranch(models.Model):
#     pass

# class Customer(models.Model):
#     name = models.CharField(max_length=50)

class MainAbstractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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
    registration_date = models.DateField()
    begin_date = models.DateField()
    end_date = models.DateField()

    car = models.ForeignKey('Car', on_delete=models.PROTECT,
                            verbose_name=_('Car'))

    insurance_code = IntegerRangeField(min_value=100, max_value=500)

    sum_insured = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    bonus = models.CharField(max_length=1, blank=True, null=True)

    territory = models.TextField()

    class Meta:
        verbose_name = _('Insurance Policy')
        verbose_name_plural = _('Insurance Polices')

    def __str__(self):
        return f'{self.number}'


class Car(MainAbstractModel):
    mark = models.CharField(max_length=50, verbose_name=_('Mark'))
    model = models.CharField(max_length=50, verbose_name=_('Model'))
    registration_place = models.CharField(
        max_length=50, verbose_name=_('Registration Place'))
    registration_country = CountryField(
        default=DEFAULT_COUNTRY_OF_CAR_REGISTRATION)
    registration_number = models.CharField(
        max_length=50, verbose_name=_('Registration Number'))
    vin_code = models.CharField(max_length=17, verbose_name=_('VIN code'))

    def __str__(self):
        return f'{self.mark} {self.model} ({self.registration_number})'


class DataFile(MainAbstractModel):
    date_format = '%d.%m.%Y'
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
                            car = Car.objects.get(
                                registration_number=row[22],
                                vin_code=row[23])
                        except ObjectDoesNotExist:
                            car = Car(
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
                                number=row[6], sticker=row[7],
                                registration_date=self.parse_date(row[8], self.date_format),
                                begin_date=self.parse_date(row[9], self.date_format),
                                end_date=self.parse_date(row[10], self.date_format),
                                car=car,
                                insurance_code=row[11],
                                sum_insured=self.parse_number(row[24]),
                                price=self.parse_number(row[25]),
                                bonus=row[26],
                                territory=row[27],
                            )
                            policy.save()
