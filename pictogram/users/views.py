from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def home(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form saved cool')
            form.save()
            print('saved form, check admin')
            messages.success(request, 'Registration suceessful. You can now login')
            # redirect('')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})