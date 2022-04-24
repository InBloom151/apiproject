from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created', 'user')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created', 'user', 'post', 'parent')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
