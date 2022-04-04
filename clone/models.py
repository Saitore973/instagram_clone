from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


#Choices
LIKE_CHOICE = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePhoto = CloudinaryField('image')
    bio = models.TextField(max_length=200, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
    
    def num_image(self):
        return self.profile.all().count()
    
    
        
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update(self, profilePhoto, bio):
        self.bio = bio
        self.profilePhoto = profilePhoto
        self.save()

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=20)
    caption = models.TextField()
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile',null=True)
    
    
    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.name 
    
    def num_likes(self):
        return self.liked.all().count()
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, caption, name):
        self.caption = caption
        self.name = name
        self.save()
    

    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICE,default='Like',max_length=10)
    
    def __str__(self):
        return self.image
    
    
class Comment(models.Model):
    image = models.ForeignKey(Image, related_name="comments",on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
    
