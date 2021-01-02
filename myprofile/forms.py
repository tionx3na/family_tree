#MyProfile Forms.py
from django import forms
from login.models import *
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, auth
import datetime

#DataFlair #Form

class DateInput(forms.DateInput):
    input_type = 'date'                                 # Passing html5 Date widget to forms as widget


class MyProfile(forms.Form):

    CHOICES = (
        ('Not Entered', 'Choose'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )


    first_name = forms.CharField(max_length=20,  required = False, label='First Name')
    middle_name = forms.CharField(max_length=20, required=False, label='Middle Name')
    last_name = forms.CharField(max_length=20, required=False, label='Last Name')
    nick_name = forms.CharField(max_length=20, required=False, label= 'Nick Name')
    thumbnail = forms.FileField(label='Upload a profile Picture')
    mobile1 = forms.CharField(min_length=7, required=False, label='Mobile Number 1', validators=[RegexValidator('^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed")])
    mobile2 = forms.CharField(min_length=7, required=False, label='Mobile Number 2',  validators=[RegexValidator('^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed")])
    Whatsapp = forms.CharField(min_length=7, required=False, label='Whatsapp Number',  validators=[RegexValidator('^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed")])
    email = forms.CharField(max_length=100, required=False, label='E-mail Address')
    father = forms.CharField(max_length=50, required=False, label='Father\'s Name')
    mother = forms.CharField(max_length=50, required=False, label='Mothers\'s Name')
    address = forms.CharField(max_length=500, required=False, widget=forms.Textarea, label='Residence Address')
    temp_address = forms.CharField(max_length=500, required=False, widget=forms.Textarea, label='Temporary Residence Address')
    parish = forms.CharField(max_length=20, required=False, label='Parish')
    dob = forms.DateField(widget=DateInput, required=False, label='Date of Birth', initial=datetime.date.today)
    blood = forms.CharField(required=False, label='Blood Group',  widget=forms.Select(choices=CHOICES))
    occupation = forms.CharField(max_length=100, required=False, label='Occupation')
    company = forms.CharField(max_length=100, required=False, label='Company Name')
    occupation_place = forms.CharField(max_length=500, required=False, label='Place of Occupation')
    spouse_name = forms.CharField(max_length=50, required=False, label='Name of Spouse')
    spouse_father = forms.CharField(max_length=50, required=False, label='Spouse Father Name')
    spouse_mother = forms.CharField(max_length=50, required=False, label='Spouse Mother Name')
    wedding_date = forms.DateField(widget=DateInput, required=False, label= 'Wedding Date', initial=datetime.date.today)
    #children_number = forms.CharField(max_length=20, required=False, label='Number Of children')
    #child1 = forms.CharField(max_length=20, required=False)
    #child2 = forms.CharField(max_length=20, required=False)
    #child3 = forms.CharField(max_length=20, required=False)
    #child4 = forms.CharField(max_length=20, required=False)



    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')




class UpdatePass(forms.Form):
    username = forms.CharField(max_length=20, required=False, label='User Name')
    password = forms.CharField(min_length=7, validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('username')
        password = cleaned_data.get('password')
