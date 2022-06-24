from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.

def login(request):
    # request == POST
    # 로그인 시키기
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    
    # request == GET
    # login html 띄우기
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')