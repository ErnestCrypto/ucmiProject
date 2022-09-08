from .serializers import FormSerializer, SubscriptionSerializer
from rest_framework import generics
from django.shortcuts import render
from.models import Form, Subscription
# Create your views here.


class Formlist(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer


class Subscriiptionlist(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
