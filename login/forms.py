from django import forms
from register.models import *

#DataFlair #Form

class Login(forms.Form):
    name = forms.CharField(max_length=50, required = True)
    attrs = {
        "type": "password"
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
