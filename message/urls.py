from django.urls import path
from django.http import HttpResponse

def message(request):
    return HttpResponse('First App')

urlpatterns =[
    path('',message , name='message'),
]