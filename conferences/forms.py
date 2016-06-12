from django import forms


class RegistrationForm(forms.Form):
    CHOICES = ((False, 'Visitor'), (True, 'Speaker'))
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial=False)
    subject = forms.CharField(max_length=100)
    about = forms.CharField(widget=forms.Textarea)
