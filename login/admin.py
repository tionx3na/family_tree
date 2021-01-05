from django.contrib import admin
from . models import *

# Register your models here.
class ActiveAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'email')
    search_fields = ('user__username', 'first_name', 'email')

admin.site.register(ActiveInvite, ActiveAdmin)
