from django.contrib import admin
from .models import Image, Comment,Like, Profile
# Register your models here.

admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Profile)