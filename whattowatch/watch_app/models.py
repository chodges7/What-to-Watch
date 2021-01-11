from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# from https://testdriven.io/blog/django-custom-user-model/
class CustomUser(AbstractUser):
    username = None
    bio = models.CharField(max_length=500)
    image = models.ImageField(default='LogoColor.png', null=True, blank=True,
    upload_to='whattowatch/watch_app/static/profile-pic')
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
