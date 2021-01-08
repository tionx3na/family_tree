from django import forms


#DataFlair #Form
class Register(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    comment = forms.CharField(max_length=500, required = False, )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

class NewUser(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    attrs = {
        "type": "password"
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))
