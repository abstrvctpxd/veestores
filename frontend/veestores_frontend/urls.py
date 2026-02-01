from django.urls import path
from django.views.generic import TemplateView
from django.http import HttpResponse
import os
from django.shortcuts import render

def index(request):
    backend_api = os.environ.get('BACKEND_API', 'veestoresbcknd.onrender.com')
    return render(request, 'index.html', {'BACKEND_API': backend_api})

def health(request):
    return HttpResponse('ok')

urlpatterns = [
    path('', index, name='index'),
    path('health/', health, name='health'),
]
