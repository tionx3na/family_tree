from django import forms
from register.models import *

#DataFlair #Form

class Login(forms.Form):
    name = forms.CharField(max_length=50, required = True)
    password = forms.CharField(max_length=100, required=True)


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
