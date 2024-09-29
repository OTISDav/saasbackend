from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class PhoneEmailAuthBackend(BaseBackend):
    def authenticate(self, request, phone_or_email=None, password=None, **kwargs):
        if phone_or_email is None or password is None:
            return None

        try:
            if '@' in phone_or_email:
                user = CustomUser.objects.get(email=phone_or_email)
            else:
                user = CustomUser.objects.get(phone_number=phone_or_email)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
