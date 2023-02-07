from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_name, name='get_name'),
    path('1', views.get_contact, name='get_contact'),
    path('validations', views.validations, name='validations'),
    path('formset_view', views.formset_view, name='formset_view'),
    path('time_date', views.time_date, name='time_date'),
    path('date_formatshow', views.date_formatshow, name='date_formatshow'),
    path('thanks/', views.thanks, name='thanks'),
]
