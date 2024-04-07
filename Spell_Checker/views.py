from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def aboutUS(request):
    return HttpResponse("This Application is developed by Mr. Mukul Jain")