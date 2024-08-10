
from django.urls import path
from .views import homepagemessage


urlpatterns = [
    path('', homepagemessage ),

]
