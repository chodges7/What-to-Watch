from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from imdb import IMDb

from .managers import CustomUserManager

# from https://testdriven.io/blog/django-custom-user-model/
class CustomUser(AbstractUser):
    username = None
    bio = models.CharField(max_length=500)
    profile_picture = models.ImageField(default='LogoColor.png', null=True, blank=True,
    upload_to='profile-pics')
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Movie(models.Model):
    title = models.CharField(null=False, max_length=50)
    rotten_tomatos = models.FloatField(blank=True, null=True)
    hulu_url = models.CharField(blank=True, max_length=100)
    amazon_url = models.CharField(blank=True, max_length=100)
    hbo_max_url = models.CharField(blank=True, max_length=100)
    netflix_url = models.CharField(blank=True, max_length=100)
    movie_id = models.IntegerField(null=False)

    def set_movie_id(self):
        movies_data = IMDb()
        search = movies_data.search_movie(self.title)
        self.movie_id = search[0].getID()

    def __str__(self):
        return self.title
