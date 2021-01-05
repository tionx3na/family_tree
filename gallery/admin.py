from django.contrib import admin
from . models import *

# Register your models here.

class AddAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title', 'user')


class PicturesAdmin(admin.ModelAdmin):
    search_fields = ('add__user', 'add__title')


admin.site.register(Pictures, PicturesAdmin)


admin.site.register(Add,AddAdmin)

