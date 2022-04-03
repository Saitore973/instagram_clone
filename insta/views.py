from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Profile
# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def photos(request):
    
    photos =Post.objects.all()
    return render(request, 'all-insta/photos.html', {"photos": photos})

def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'all-insta/results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'all-insta/results.html', {'message': message})