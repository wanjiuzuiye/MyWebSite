from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

"""主页视图"""
def index(request):
    # 模拟数据
    total_data = 220 
    total_used = 180
    today_data = 100
    today_used = 50
    contex = {
        'total_data': total_data,
        'total_used': total_used,
        'today_data': today_data,
        'today_used': today_used,
    }
    return render(request, 'index.html', contex)

def buttons(request):
    return render(request, 'pages/ui-features/buttons.html')

def typography(request):
    return render(request, 'pages/ui-features/typography.html')

def basic_elements(request):
    return render(request, 'pages/forms/basic_elements.html')

def chartjs(request):
    return render(request, 'pages/charts/chartjs.html')

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