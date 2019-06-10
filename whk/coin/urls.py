from django.urls import path
from . import views

app_name = 'coin'

urlpatterns = [
    path('', views.list, name="list")
]