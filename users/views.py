from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout as auth_logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm, UserProfile
from .models import UserProfile

# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            return HttpResponse("Passwords do not match")
        
        if User.objects.filter(username = username).exists():
            return HttpResponse("Username exist")
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()

        auth_login(request, user)

        return redirect('login')
    
    return render(request , 'registration/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        
        else:
            return HttpResponse("invalid login")
        
    return render(request, 'registration/login.html')

def user_logout(request):
    auth_logout(request)

    return redirect('login')


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            user_image = form.save(commit=False)
            user_image.user = request.user
            user_image.save()
            return redirect('home')
        
        else:
        #     form = ImageUploadForm()

        # return render(request,'upload_image.html',{'form':form})

            return render(request,'upload_image.html',{'form':form})
    
    else:
        form = ImageUploadForm()
        return render(request,'upload_image.html',{'form':form})

        
@login_required
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfile(request.POST,request.FILES , instance = user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        
        else:
            form = UserProfile(instance=user_profile)

        # return render(request,'upload_image.html',{'form':form})

            return render(request,'upload_image.html',{'form':form})
    
    else:
        form = ImageUploadForm()
        return render(request,'upload_image.html',{'form':form})

        