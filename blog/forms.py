# Family event Forms.py
from django import forms
from blog.models import *


from tinymce.widgets import TinyMCE



categories = (
        ('1', 'Family'),
        ('2', 'Personal'),
        ('3', 'Political')
    )




class Blog(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Title')
    overview = forms.CharField(max_length=500, required=True, widget=forms.Textarea, label='Overview (under 500 words)')
    category = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=categories)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post







    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        title = cleaned_data.get('title')
        date = cleaned_data.get('date')
        content = cleaned_data.get('content')

