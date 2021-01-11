from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from . import models

# class ProfileForm(forms.Form):
#     profile_bio = forms.CharField(label='Your new Bio', max_length=500)
#     profile_fname = forms.CharField(label='Your corrected first name', max_length=50)
#     profile_lname = forms.CharField(label='Your corrected last name', max_length=50)
#
# class SearchForm(forms.Form):
#     search_field = forms.CharField(label='Search any movie', max_length=50)
#
# class BioForm(forms.Form):
#     profile_bio = forms.CharField(label='Your new Bio', max_length=500)
#
# class PictureForm(forms.Form):
#     profile_image = forms.ImageField(label='Your new picture')

# from https://testdriven.io/blog/django-custom-user-model/
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = models.CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.CustomUser
        fields = ('email',)
