from django.contrib import admin
from .models import Form, Subscription
# Register your models here.


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['Fullname',
                    'Emailaddress',
                    'Phonenumber',
                    'Formtype',
                    'Message']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['subscription']
