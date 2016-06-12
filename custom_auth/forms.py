from custom_auth.models import Profile
from django.contrib.auth.models import User
from django import forms


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']