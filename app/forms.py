from django import forms
from .models import Video,  Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file', 'description']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']