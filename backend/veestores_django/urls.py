from django.urls import path
from django.http import HttpResponse
from django.contrib import admin

def index(request):
    return HttpResponse('veestores backend (Django) is running')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
