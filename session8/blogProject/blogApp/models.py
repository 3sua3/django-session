from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length= 200)
    content = models.TextField()
    category = models.CharField(max_length=10, null = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name="comments")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content
    
class Recomment(models.Model):
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name="recomments")
    recontent = models.TextField()

    def __str__(self):
        return self.recontent


