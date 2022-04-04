from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ImageForm, CommentForm, ProfileForm, SearchForm
from .models import Image, Comment, Profile
# Create your views here.

#Landing Page
@login_required(login_url='login')
def index(request):
    posts = Image.objects.all()
    form = CommentForm()
    searchform = SearchForm()
    userid = request.user.id
    if request.method == 'POST':
        searchform = SearchForm(request.POST)
        if searchform.is_valid():
            name = searchform.cleaned_data['name']
            profile = Profile.objects.get(user__username=name)
            userid = request.user.id
            return render(request, 'app/profile.html',{"profile":profile, "userid":userid})
    return render(request, 'app/index.html',{"title":"Home","posts":posts,"form":form,"userid":userid,"searchform":searchform})

#Register Form
def register(request):
    form = RegisterForm()
    userid = request.user.id
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    
    return render(request, 'registration/register.html', {"form":form, "userid":userid})

def profile(request, id):
    profile = Profile.objects.get(user=id)
    userid = request.user.id

    return render(request, 'app/profile.html',{"profile":profile, "userid":userid})


#Create Post Form
@login_required(login_url='login')
def create(request):
    form = ImageForm()
    userid = request.user.id
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            name = form.cleaned_data['name']
            caption = form.cleaned_data['caption']
            user_of_post = request.user
            post = Image(image=image,name=name, caption=caption,user=user_of_post,profile=user_of_post.profile)
            post.save()
            return redirect('home')
    return render(request, 'app/create.html', {"form":form,"userid":userid})

#Comment form
def comment(request, id):
    image = Image.objects.get(id=id)
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        comment_new = Comment(image=image,name=user, comment=comment)
        comment_new.save()
        return redirect('single',image.id)
    
    
#Like Form
def like(request):
    user = request.user
    if request.method == "POST":
        image_id = request.POST.get('image_id')
        image_obj = Image.objects.get(id=image_id)
        
        if user in image_obj.liked.all():
            image_obj.liked.remove(user)
        else:
            image_obj.liked.add(user)
    return redirect('home')


#Single Form
@login_required(login_url='login')
def single(request, id):

    post = Image.objects.get(id=id)
    form = CommentForm()
    userid = request.user.id
    return render(request, 'app/single.html', {'post':post,"userid":userid,"form":form})




def edit(request, id):
    profile = Profile.objects.get(id=id)
    form = ProfileForm(instance=profile)
    userid = request.user.id
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            # instance.user = Profile.objects.get(user=request.user)
            instance.save()
            return redirect(f'profile/{userid}/')
    return render(request, 'app/edit.html', {"form":form})


