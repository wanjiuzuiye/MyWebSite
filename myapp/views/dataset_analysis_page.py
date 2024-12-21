from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def basic_table(request):
    return render(request, 'pages/tables/basic-table.html')

def mdi(request):
    return render(request, 'pages/icons/mdi.html')

def l(request):
    return render(request, 'pages/samples/login.html')

def login_2(request):
    return render(request, 'pages/samples/login-2.html')

def register(request):
    return render(request, 'pages/samples/register.html')

def register_2(request):
    return render(request, 'pages/samples/register-2.html')

def lock_screen(request):
    return render(request, 'pages/samples/lock-screen.html')

def documentation(request):
    return render(request, 'documentation/documentation.html')