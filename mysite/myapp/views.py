from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.list import ListView

from .models import Person, Fruits, Person1, Group, Membership
from .forms import ShirtForm, FruitsForm, PGMGroupForm, PGMPersonForm, PGMMemberForm


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


class PGMPerson(generic.CreateView):
    model = Group
    form_class = PGMGroupForm
    template_name = 'myapp/PGMPerson.html'
    success_url = reverse_lazy('shirtapp:pgmperson')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form2'] = PGMMemberForm(self.request.POST or None)
        return context

    def form_valid(self, form):
        form1 = form.save()
        context = self.get_context_data()
        form2 = context['form2']
        if form2.is_valid():
            person = Person1.objects.create(name=form2.cleaned_data['person1'])
            member = Membership.objects.create(person=person, group=form1,
                                               date_joined=form2.cleaned_data['date_joined'],
                                               invite_reason=form2.cleaned_data['invite_reason'])

        return super().form_valid(form)


class PGMPersonresult(ListView):
    model = Person1
    template_name = 'myapp/PGMPersonresult.html'
    queryset = Person1.objects.all()
    context_object_name = 'personpgm'


class PGMGroup(generic.CreateView):
    model = Group
    form_class = PGMGroupForm
    template_name = 'myapp/PGM_Group.html'
    success_url = 'shirtapp:pgmgroup'


class PGMGroupresult(ListView):
    model = Group
    template_name = 'myapp/PGM_Groupresult.html'
    queryset = Person1.objects.all()
    context_object_name = 'grouppgm'
