from django.contrib import admin
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from .models import InsurancePolicy, Car, DataFile, Customer


@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ['number', 'registration_date', 'begin_date', 'end_date',
                    'get_insurance_code', 'get_customer',
                    'get_car', 'sum_insured',
                    'price', 'get_territory']
    ordering = ['id']

    def get_insurance_code(self, obj):
        return obj.insurance_code
    get_insurance_code.short_description = _('Code')

    def get_customer(self, obj):
        link = reverse("admin:customer_service_customer_change",
                       args=[obj.customer.id])
        return mark_safe('<a href="%s">%s</a>' % (link, obj.customer))
    get_customer.allow_tags = True
    get_customer.short_description = _('Customer')

    def get_car(self, obj):
        link = reverse("admin:customer_service_customer_change",
                       args=[obj.car.id])
        return mark_safe('<a href="%s">%s</a>' % (link, obj.car))
    get_car.allow_tags = True
    get_car.short_description = _('Car')

    def get_territory(self, obj):
        return obj.territory[:10]
    get_territory.short_description = _('Territory')



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'registration_place',
                    'registration_country', 'registration_number', 'vin_code')
    ordering = ['id']


@admin.register(DataFile)
class CarAdmin(admin.ModelAdmin):
    list_display = ('file', 'created')
    ordering = ['id']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_customer_type', 'get_ind_number', 'address',
                    'country', 'phone')
    ordering = ['id']

    def get_customer_type(self, obj):
        return obj.customer_type
    get_customer_type.short_description = _('Type')

    def get_ind_number(self, obj):
        return obj.ind_number
    get_ind_number.short_description = _('IIN')

