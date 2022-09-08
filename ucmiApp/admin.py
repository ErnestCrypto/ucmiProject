from django.contrib import admin
from .models import Form, Subscription
# Register your models here.


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['fullname',
                    'emailaddress',
                    'phonenumber',
                    'formtype',
                    'message']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['emailaddress', 'subscription']
