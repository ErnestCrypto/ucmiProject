from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from .token import token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .serializers import FormSerializer, SubscriptionSerializer
from rest_framework import generics
from django.shortcuts import render
from.models import Form, Subscription
# Create your views here.


def sendActivationEmail(email_person, request):
    try:
        user = Subscription.objects.get(emailaddress=email_person)
    except Exception as e:
        user = None
    current_site = get_current_site(request)
    email_subject = 'Activate Your Account'
    email_body = render_to_string(
        'account_activation.html',
        {
            'domain': current_site.domain,
            'uid': user.id,
            'token': token_generator.make_token(user),
        }
    )
    email = EmailMessage(subject=email_subject, body=email_body, from_email=settings.EMAIL_HOST_USER,
                         to={user.emailaddress}
                         )
    email.send()


def activate_user(request, uid64, token):
    try:
        uid = uid64
        user = Subscription.objects.get(id=uid)
    except Exception as e:
        user = None
    if user or token_generator.check_token(user, token):
        user.subscription = "True"
        user.save()
        return render(request, 'account.html')
    else:
        return render(request, 'activate_failed.html')


@api_view(['GET', 'POST'])
def subscriptionList(request):
    if request.method == 'GET':
        subscription = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            email = data.get('emailaddress')
            serializer.save()
            sendActivationEmail(email, request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Formlist(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
