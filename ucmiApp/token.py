# Token generator
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import Subscription
import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.id)
            + six.text_type(timestamp)
        )


token_generator = AccountActivationTokenGenerator()
