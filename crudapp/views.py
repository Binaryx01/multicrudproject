from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    
    return render(request, 'crudapp/create_post.html', {'form': form})
        


def register_user(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login_user'))
    else:
        form = UserCreationForm()
        return render(request,'crudapp/register_user.html',{'form':form})
    
    
def index(request):
    posts = Post.objects.all()
    return render(request,'crudapp/index.html',{'posts':posts})
    

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # Check if authentication is successful
            user = form.get_user()
            login(request, user)
            return redirect(reverse_lazy('index'))
    else:
        form = AuthenticationForm()
        
    return render(request, 'crudapp/login_user.html', {'form': form})
    
def logout_user(request):
    logout(request)
    return redirect('index')
    