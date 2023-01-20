from django.urls import path
from . import views

app_name = 'shirtapp'

urlpatterns = [
    path('', views.Personshirt.as_view(), name='myapphome'),
    path('list', views.PersonShirtList.as_view(), name='shirtlist'),
    path('fruitlist', views.Fruitsname.as_view(), name='fruitlist'),
    path('fruit', views.Fruit.as_view(), name='fruit'),
    path('pgmperson/', views.PGMPerson.as_view(),name= 'pgmperson'),
    path('pgmpersonresult/', views.PGMPerson.as_view(),name= 'pgmpersonresult'),
    path('pgmgroup/', views.PGMPerson.as_view(), name='pgmgroup'),
    path('pgmgroupresult/', views.PGMPerson.as_view(),name= 'pgmgroupresult'),
]
