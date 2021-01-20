from django.contrib import admin
from django.contrib.auth.models import  Group
from . models import *
from django.core.mail import EmailMessage                                   # For e-mail
from django.conf import settings
from django.template.loader import render_to_string                         # For rendering to string
from django.contrib import messages                                         # For admin page pop up after send_email
from django.contrib.auth.models import User
from login.models import ActiveInvite


# Register your models here.
admin.site.site_header = 'Erupakkatu Family Admin Dashboard'
admin.site.unregister(Group)


def send_mail (modeladmin,request,queryset):
    # Automated e-mailing of invite code from Admin Panel
    for obj in queryset:
         body = render_to_string('register/register_email.html', {'obj': obj})  # Template for rendering e-mail
         email = EmailMessage(
             'Eruppakkatu Family Blog Activation Code',
             body,
             settings.EMAIL_HOST_USER,
             [obj.email],                                  # To Adrress should be a tuple otherwise error occurs
         )
         email.fail_silently = False
         email.send()
         inv_code = str(obj.invite_code)
         user = User.objects.create_user(username=obj.name, password=inv_code, email=obj.email, first_name=obj.name)
         user.save()
         PendingInvite.objects.filter(invite_code=obj.invite_code).delete()



    messages.add_message(request, messages.INFO, 'Verification E-mail Has been sent!')  # display popup messsage


class PendingInviteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment')
    actions= [send_mail]



admin.site.register(PendingInvite, PendingInviteAdmin)                  # Registering The model and overriding
