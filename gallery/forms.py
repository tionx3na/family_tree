from django import forms
from .models import *
from django.forms import inlineformset_factory



class Album(forms.Form):
    title = forms.CharField(max_length=50, required = True, label='Title of the Album')
    description = forms.CharField(max_length=100000, required=True, widget=forms.Textarea, label='Description about the album')
    thumbnail = forms.FileField(label='Upload the Thumbnail for the Album')
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Upload multiple images or videos')


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')