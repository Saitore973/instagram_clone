from django.db import models

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=44, null=True)
    bio = models.TextField()
    posts = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)