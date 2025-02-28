from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=50)

class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    tags=models.ManyToManyField(Tag,related_name='posts',blank=True)

class Comment(models.Model):
    post=models.ForeignKey(BlogPost,related_name='comments',on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


