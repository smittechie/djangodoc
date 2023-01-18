from django.shortcuts import render
from django.views import generic

from mysite.myapp.models import Person


# Create your views here.
class Personshirt(generic.DetailView):
    model = Person

