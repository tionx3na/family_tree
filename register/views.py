from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from . import forms
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    form = forms.Register()
    if request.method == 'POST':                            # POST request processing
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        try:
            user = User.objects.get(username__exact=name)
        except User.DoesNotExist:
            user = None
        if user:
            error = "Name Already exists!"
            return render(request, 'register/register_form.html', {'form': form, 'error':error})
        else:
            pendinginvite = PendingInvite()                     # Initializing Table for data entry
            pendinginvite.name = name
            pendinginvite.email = email
            pendinginvite.comment = comment
            pendinginvite.save()                                # Saving data into the table
            return redirect('redirected')                        # Redirect URL

    else:
         return render(request, 'register/register_form.html', {'form': form})          # Render URL


def redirected(request):
    return render(request, 'register/register_redirect.html')


def more_info(request):
    return render(request, 'register/more_info.html')