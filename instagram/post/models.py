from django.db import models


class Post(models.Model):
    photo = models.ImageField(upload_to='photo')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.photo} - {self.created_at}'


class PostComment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
