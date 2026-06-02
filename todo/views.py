from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods

def index(request):
    return HttpResponse("Домашняя страница.")

def register(request) -> HttpResponse:
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else: # GET
        form = RegistrationForm()
    context = {"form": form}
    return render(request, template_name="todo/register.html", context=context)