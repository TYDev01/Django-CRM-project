from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Login succesfully')
            return redirect('home')
        else:
            messages.warning(request, 'Account not found')
            return redirect('login_view')
    else:
        return render(request, 'login.html')
    
    # return render(request, 'home.html')


# Logout function

def logout_user(request):
    logout(request)
    messages.success(request,"logout successfully.")
    return redirect('home')
