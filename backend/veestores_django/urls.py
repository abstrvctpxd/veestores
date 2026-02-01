from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse('veestores backend (Django) is running')

urlpatterns = [
    path('', index),
]
