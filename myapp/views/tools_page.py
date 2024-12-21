from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def chartjs(request):
    return render(request, 'pages/charts/chartjs.html')