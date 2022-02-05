from django.shortcuts import render
from .forms import RegisterForm

def home(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form saved cool')

    else:
        form = RegisterForm()
        
    return render(request, 'users/register.html', {'form': form})