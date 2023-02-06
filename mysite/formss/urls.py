from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_name, name='get_name'),
    path('1', views.get_contact, name='get_contact'),
    path('validations', views.validations, name='validations'),
    path('thanks/', views.thanks, name='thanks'),
]
