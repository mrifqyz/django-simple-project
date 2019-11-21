from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

def register(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST);
        username = request.POST['username'];
        password = request.POST['password1'];

        if(form.is_valid()):
            User.objects.create_user(username=username, password=password);
            return redirect('/')

    else:
        form = UserCreationForm()

    return render(request, 'register.html',{'form':form})

def loginUser(request):
    if(request.method == 'POST'):
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            request.session.set_expiry(300)
            login(request, user);   
            return redirect('/')

    else:
        form = UserForm()

    return render(request, 'login.html', {'form':form})

def logoutUser(request):
    logout(request)
    return redirect(reverse(loginUser))


