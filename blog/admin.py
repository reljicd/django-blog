from django.contrib import admin

from blog.models.comment import Comment
from blog.models.post import Post

admin.site.register(Post)
admin.site.register(Comment)
