from django.contrib import admin
from familyevents.models import *

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'author')


admin.site.register(FamilyEvent,EventAdmin)