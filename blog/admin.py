from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timestamp')
    search_fields = ('title', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'comment', 'user__username')


admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentAdmin)
