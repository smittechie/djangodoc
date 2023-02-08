from django.urls import path

from . import views

app_name = 'templateapi'

urlpatterns = [
    path('', views.templateapi, name='templateapi'),
]
