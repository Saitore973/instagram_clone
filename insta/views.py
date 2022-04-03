from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def photos(request):
    
    photos =Image.objects.all()
    return render(request, 'all-insta/photos.html', {"photos": photos})