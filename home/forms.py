from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Art

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ArtSubmissionForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = '__all__'
        exclude = ['approved', 'likes', 'user']