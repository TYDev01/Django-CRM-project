from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

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


# def register_user(request):
#     form = SignUpForm()
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Account created successfully")
#             return redirect('login')
#         else:
#             messages.warning(request, 'Fill up the required details')
#             return redirect('Register')
#     else:
#         form = SignUpForm()
#         return render(request, 'Register.html', {'form':form})
#     return render(request, 'Register.html',)

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('login_view')
        else:
            # Form is invalid, display errors to the user
            messages.warning(request, 'Please correct the errors below.')
    else:
        # GET request or invalid form, display the registration form
        form = SignUpForm()
    return render(request, 'Register.html', {'form': form})