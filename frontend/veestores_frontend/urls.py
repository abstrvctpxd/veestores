from django.urls import path
from django.views.generic import TemplateView
from django.http import HttpResponse

def health(request):
    return HttpResponse('ok')

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('health/', health, name='health'),
]
