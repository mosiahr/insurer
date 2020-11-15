from django.db import models
from django.utils.translation import ugettext as _

from django_countries.fields import CountryField

from insurer.settings import DEFAULT_COUNTRY_OF_CAR_REGISTRATION


# class CompanyDirectorate(models.Model):
#     pass
#
#
# class CompanyBranch(models.Model):
#     pass


class IntegerRangeField(models.PositiveSmallIntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.PositiveSmallIntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class InsurancePolicy(models.Model):
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

    creating_record_date = models.DateTimeField(auto_now_add=True)
    updating_record_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Insurance Policy')
        verbose_name_plural = _('Insurance Polices')


class Car(models.Model):
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

# class Customer(models.Model):
#     name = models.CharField(max_length=50)
