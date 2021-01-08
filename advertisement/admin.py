from django.contrib import admin
from .models import Advertisement, Adinpage, Thought

# Register your models here.
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title', 'link')

class AdInAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title', 'link')

admin.site.register(Adinpage, AdInAdmin)

admin.site.register(Advertisement, AdAdmin)

admin.site.register(Thought)
