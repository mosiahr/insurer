from django.contrib import admin

from .models import InsurancePolicy, Car


@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ['number', 'registration_date', 'begin_date', 'end_date',
                    'car', 'get_info_car', 'insurance_code', 'sum_insured', 'price', 'territory']
    ordering = ['id']

    @staticmethod
    def get_info_car(_):
        return f'VIN: {_.car.vin_code}'


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'registration_place',
                    'registration_country', 'registration_number', 'vin_code')
    ordering = ['id']


