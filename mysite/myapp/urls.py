from django.urls import path
from . import views

app_name = 'shirtapp'

urlpatterns = [
    path('', views.Personshirt.as_view(), name='myapphome'),
    path('list', views.PersonShirtList.as_view(), name='shirtlist'),
    path('fruitlist', views.Fruitsname.as_view(), name='fruitlist'),
    path('fruit', views.Fruit.as_view(), name='fruit'),
]
