# Family event Forms.py
from django import forms
from familyevents.models import *
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

class Event(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Title')
    date = forms.DateField(widget=DateInput, required=True, label='Date', initial=datetime.date.today)
    content = forms.CharField(max_length=100000, required=True, widget=forms.Textarea, label='Event Content')
    thumbnail = forms.FileField(label='Upload an event thumbnail')



    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        title = cleaned_data.get('title')
        date = cleaned_data.get('date')
        content = cleaned_data.get('content')

