from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# from https://testdriven.io/blog/django-custom-user-model/
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    profile_bio = models.CharField(max_length=500)
    profile_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='watch/static/profile-pics',
        default='LogoColor.png', null=True, blank=True)

    def __str__(self):
        return profile_user
