# Family event Forms.py
from django import forms
from blog.models import *


from tinymce.widgets import TinyMCE






class Blog(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Title')
    thumbnail = forms.FileField(label='Upload the Thumbnail for the Blog', required=False, initial='thumbnail.jgp')
    overview = forms.CharField(max_length=500, required=False, widget=forms.Textarea, label='Overview (under 500 words)')
    tag = forms.CharField(max_length=20, required=True, label='Tag')
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post







    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        title = cleaned_data.get('title')
        overview = cleaned_data.get('overview')
        date = cleaned_data.get('date')
        content = cleaned_data.get('content')

