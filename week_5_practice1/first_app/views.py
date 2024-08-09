from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
# Create your views here.

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user' : request.user})
    else:
        return redirect('loginpage')

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.Register(request.POST)
            if form.is_valid():
                form.save()
                return redirect('loginpage')
        else:
            form = forms.Register()
        return render(request, 'register.html', {'form' : form, 'type' : 'Sign Up'})
    else:
        return redirect('profilepage')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = name, password = user_pass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return redirect('profilepage')
        else:
            form =  AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})
    else:
        return redirect('profilepage')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('homepage')

def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Profile updated successfully')
                form.save()
                return redirect('profilepage')
        else:
            form = forms.ChangeUserData(instance = request.user)
            return render(request, 'edit_profile.html', {'form' : form})
    else:
        return redirect('registepage')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password updated successfully')
                update_session_auth_hash(request, request.user)
                return redirect('profilepage')
        else:
            form = PasswordChangeForm(user= request.user)
            return render(request, 'pass_change.html', {'form' : form})
    else:
        return redirect('registerpage')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password updated successfully')
                update_session_auth_hash(request, request.user)
                return redirect('profilepage')
        else:
            form = SetPasswordForm(user= request.user)
            return render(request, 'pass_change.html', {'form' : form})
    else:
        return redirect('registerpage')