from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

def pass_user_to_acc(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        return ""
    else:
        return "User with this email doesn't exist"

def register_new_user(request):
    user_name = request.POST['first_name']
    user_last_name = request.POST['last_name']
    user_pass = request.POST['password']
    user_email = request.POST['email']
    user_username = user_email
    pass_validate = request.POST['pass_validation']
    User.objects.create_user(
        username=user_username,
        password=user_pass,
        first_name=user_name,
        last_name=user_last_name,
        email=user_email
    )

def check_user_unique(request):
    user = User.objects.filter(username = request.POST['email'])
    if request.POST['password'] != request.POST['pass_validation']:
        return "Your passwords aren't matching!"
    if len(user) == 0:
        register_new_user(request)
        return ""
    else: 
        return "User with this email already exists!"

def authorization(request):
    user = User.objects.filter(username = request.POST['email'])
    if len(user) == 0:
        return "Account doesn't exists!"
    