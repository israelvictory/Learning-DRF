from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'content']


admin.site.register(Post, PostAdmin)
