from django.db import models
# building our models


class Form(models.Model):
    Fullname = models.CharField(max_length=255)
    Emailaddress = models.EmailField()
    Phonenumber = models.CharField(max_length=255)
    Formtype = models.CharField(max_length=255)
    Message = models.TextField()


class Subscription(models.Model):
    subscription = models.CharField(max_length=255)
