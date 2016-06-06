from django.contrib.auth.models import User
from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class SignupForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'


class RegistrationForm(forms.Form):
    CHOICES = (('visitor', 'Visitor'), ('speaker', 'Speaker'))
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial='visitor')
    subject = forms.CharField(max_length=100)
    about = forms.CharField(widget=forms.Textarea)
