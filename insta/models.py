from re import M
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=44, null=True)
    bio = models.TextField()
    posts = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Image(models.Model):
    image = models.ImageField(upload_to= 'images/', default="Image")
    image_name= models.CharField(max_length=44)
    image_caption= models.TextField()
    likes = models.IntegerField(default="0")
    comments = models.TextField(default="No Comment")
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)