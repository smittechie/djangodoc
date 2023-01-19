from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.list import ListView

from .models import Person, Fruits
from .forms import ShirtForm, FruitsForm


# Create your views here.
class Personshirt(generic.CreateView):
    model = Person
    form_class = ShirtForm
    template_name = 'myapp/index.html'
    success_url = reverse_lazy('shirtapp:shirtlist')
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['form'] = ShirtForm()
    #     return context


class PersonShirtList(ListView):
    model = Person
    template_name = 'myapp/shirtlist.html'
    queryset = Person.objects.all()
    context_object_name = reverse_lazy('shirtapp:fruitlist')

class Fruit(generic.CreateView):
    model = Fruits
    form_class = FruitsForm
    template_name = 'myapp/fruitindex.html'
    success_url = 'fruitlist'

class Fruitsname(ListView):
    model = Fruits
    template_name = 'myapp/fruitslist.html'
    queryset = Fruits.objects.all()
    context_object_name = 'fruitname'
