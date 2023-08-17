from django.contrib.auth import authenticate, login as app_login, logout as app_logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    return render(request, "login.html")

def submit_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            app_login(request, user)
            return redirect('about_me')
        else:
            messages.error(request, "Login incorrect, try again!")
    return redirect("about_me")

def logout(request):
    app_logout(request)
    return redirect('about_me')
