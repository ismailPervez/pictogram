from django.shortcuts import render, redirect
from .forms import RegisterForm, CreatePostForm
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            picture = form.cleaned_data['profile_pic']
            print('form saved cool')
            form.save()
            print('saved form, check admin')
            messages.success(request, 'Registration suceessful. You can now login')
            redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = Post(
                picture=form.cleaned_data['picture'],
                caption=form.cleaned_data['caption'],
                user=request.user
            )

            new_post.save()
            messages.success(request, 'post successfully uploaded')

    else:
        form = CreatePostForm()

    return render(request, 'users/post.html', {'form': form})