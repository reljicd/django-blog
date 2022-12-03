from django.contrib.auth.models import User
from django.db import models

from blog.models.post import Post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return (f'"{self.body[:20]}..." '
                f'on {self.post.title} by {self.user.username}')
