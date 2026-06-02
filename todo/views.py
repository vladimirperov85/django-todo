from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime 
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods

def index(request):
    return HttpResponse("Домашняя страница.")
