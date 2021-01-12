from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from . import models

class SearchForm(forms.Form):
    search_field = forms.CharField(label='Search any movie', max_length=50)

class BioForm(forms.Form):
    bio = forms.CharField(label='Your new Bio', max_length=500)

class PictureForm(forms.Form):
    image = forms.ImageField(label='Your new picture')

# class from https://testdriven.io/blog/django-custom-user-model/
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = models.CustomUser
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name',
        'bio', 'image')

# class from https://testdriven.io/blog/django-custom-user-model/
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.CustomUser
        fields = ('email',)
