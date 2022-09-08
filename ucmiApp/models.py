from django.db import models
# building our models


class Form(models.Model):
    fullname = models.CharField(max_length=255)
    emailaddress = models.EmailField()
    phonenumber = models.CharField(max_length=255)
    formtype = models.CharField(max_length=255)
    message = models.TextField()


class Subscription(models.Model):
    emailaddress = models.EmailField()
    subscription = models.BooleanField(default=False)
