from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout as auth_logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm, UserProfileForm, TaskForm
from .models import UserProfile , Task
from django.core.cache import cache


# Create your views here.
@login_required
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
            # return redirect('upload_image')
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
    user_profile_key = f'user_profile_{request.user.id}'
    user_profile = cache.get(user_profile_key)
    if not user_profile:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        cache.set(user_profile_key, user_profile, timeout=60*15)  

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            cache.set(user_profile_key, user_profile, timeout=60*15)  
            # return redirect('user_profile')
            return redirect('home')

    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'user_profile.html', {'form': form, 'user_profile': user_profile})



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})
  