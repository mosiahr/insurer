from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe

from .models import InsurancePolicy, Car, DataFile, Customer, \
    MessageSmsInsurancePolicyExpires


class DisableAddChangeDeleteAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        """
        Override method to disable add the object.
        """
        return False

    def has_change_permission(self, request, obj=None):
        """
        Override method to disable change the object.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Override method to disable delete the object.
        """
        return False


@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ['number', 'registration_date', 'begin_date', 'end_date',
                    'get_insurance_code', 'get_customer',
                    'get_car', 'sum_insured',
                    'price', 'get_territory', 'get_sms']
    ordering = ['id']
    # fields = ['number', 'registration_date', 'begin_date', 'end_date',
    #           'insurance_code', 'customer',
    #           'car', 'sum_insured',
    #           'price', 'territory', 'author', 'created', 'updated']
    readonly_fields = ['author', 'created', 'updated']

    def get_insurance_code(self, obj):
        return obj.insurance_code

    get_insurance_code.short_description = _('Code')

    def get_customer(self, obj):
        if obj.customer:
            link = reverse("admin:customer_service_customer_change",
                           args=[obj.customer.id])
            return mark_safe('<a href="%s">%s</a>' % (link, obj.customer))

    get_customer.allow_tags = True
    get_customer.short_description = _('Customer')

    def get_car(self, obj):
        if obj.car:
            link = reverse("admin:customer_service_car_change",
                           args=[obj.car.id])
            return mark_safe('<a href="%s">%s</a>' % (link, obj.car))

    get_car.allow_tags = True
    get_car.short_description = _('Car')

    def get_territory(self, obj):
        return obj.territory[:10]

    get_territory.short_description = _('Territory')

    def get_sms(self, obj):
        sms = []
        message_sms_list = MessageSmsInsurancePolicyExpires.objects.filter(
            insurance_policy=obj.id)
        for message_sms in message_sms_list:
            link = reverse(
                "admin:customer_service_messagesmsinsurancepolicyexpires_change",
                args=[message_sms.pk])
            sms.append('<a href="%s">%s</a>' % (link, message_sms.created))
        return mark_safe('<br>'.join(sms))

    get_sms.allow_tags = True
    get_sms.short_description = _('SMS')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'registration_place',
                    'registration_country', 'registration_number',
                    'vin_code')
    ordering = ['id']
    readonly_fields = ['author', 'created', 'updated']


@admin.register(DataFile)
class DataFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'created', 'author')
    ordering = ['id']

    readonly_fields = ['author', 'created', 'updated']

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'get_customer_type', 'get_ind_number', 'address',
        'country', 'phone')
    ordering = ['id']

    readonly_fields = ['author', 'created', 'updated']

    def get_customer_type(self, obj):
        return obj.customer_type

    get_customer_type.short_description = _('Type')

    def get_ind_number(self, obj):
        return obj.ind_number

    get_ind_number.short_description = _('IIN')


@admin.register(MessageSmsInsurancePolicyExpires)
class MessageSmsInsurancePolicyExpiresAdmin(DisableAddChangeDeleteAdmin):
    list_display = ('sid', 'body', 'from_phone_number', 'to_phone_number',
                    'insurance_policy', 'created')
    readonly_fields = ['author', 'created', 'updated']
    list_display_links = ['sid']
