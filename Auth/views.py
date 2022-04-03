from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import LogForm, RegForm

from . import views_cases
# Create your views here.

def logging_out(request):
    logout(request)
    return redirect("home")

def logining_view(request):
    context = {
        'forms':LogForm(),
        'error':''
    }
    if request.method == 'POST':
        context['error'] = views_cases.pass_user_to_acc(request)
        return redirect("polls")
    return render(request, 'Auth/logining.html', context)

def registration_view(request):
    context = {
        'forms':RegForm(),
        'error':''
    }
    if request.method == 'POST':
        context['error'] = views_cases.check_user_unique(request)
        if context['error'] == '':
            return redirect("auth")
    return render(request, 'Auth/registration.html', context)