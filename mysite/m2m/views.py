from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView, TemplateView

from .forms import PGMGroupForm, PGMMemberForm
from .models import Group, Person, Membership


# Create your views here.
class PGM_Group(generic.CreateView):
    model = Group
    form_class = PGMGroupForm
    template_name = 'm2m/PGM_Group.html'
    success_url = reverse_lazy('m2m:pgmpersonresult')             # pgmgroupresult  ,  pgmpersonresult   pgmoptions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form2'] = PGMMemberForm(self.request.POST or None)
        return context

    def form_valid(self, form):
        form1 = form.save()
        context = self.get_context_data()
        form2 = context['form2']

        if form2.is_valid():
            # person = Person.objects.create(name=form2.cleaned_data['person'])
            person = Person.objects.create(name=form2.cleaned_data['person'])
            member = Membership.objects.create(person=person, group=form1,
                                               date_joined=form2.cleaned_data['date_joined'],
                                               invite_reason=form2.cleaned_data['invite_reason'])
        return super().form_valid(form)


class PGMPersonresult(ListView):
    model = Person
    template_name = 'm2m/PGMPersonresult.html'
    queryset = Person.objects.all()
    context_object_name = 'personpgm'


class PGMGroupresult(ListView):
    model = Group
    template_name = 'm2m/PGM_Groupresult.html'
    queryset = Group.objects.all()
    context_object_name = 'grouppgm'
#
#
# class PGMOptions(TemplateView):
#     template_name = 'm2m/PGM_Options.html'
#
#     def get_redirect_url(self):
#         if self.request.GET.get('choice'):
#             return reverse('m2m:pgmgroupresult')
#         else:
#             return reverse('m2m:pgmoptions')
#
#
#     def get_queryset(self):
#
#         keyword = self.request.GET.get('choice')
#         if keyword == 'Person':
#             list_pgm = Person.objects.all()
#         else:
#             list_pgm = Group.objects.all()
#         return list_pgm