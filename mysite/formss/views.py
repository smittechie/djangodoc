from django.core.exceptions import ValidationError
from django.forms import modelformset_factory, modelform_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from .forms import NameForm, ContactForm, AuthorForm, TimeDateForm
from .models import Author, TimeDate


# Create your views here.
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'formss/name.html', {'form': form})


def get_contact(request):
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form1 = ContactForm()
    return render(request, 'formss/contact.html', {'form1': form1})


def thanks(request):
    context = 'Hello HttpResponse'
    return render(request, 'formss/thanks.html', {'context': context})


def validations(request):
    if request.method == 'POST':
        auth_form = AuthorForm(request.POST)
        if auth_form.is_valid():
            return HttpResponseRedirect("thanks/")
    else:
        auth_form = AuthorForm()

    return render(request, 'formss/author.html', {'auth_form': auth_form})


def formset_view(request):
    context = {}

    # creating a formset
    """  # AuthorFormSet = modelformset_factory(AuthorForm)
    # formset = AuthorFormSet"""  ## old tried from gfg

    AuthorFormSet = modelformset_factory(Author, fields=('__all__'))  ##single form
    # AuthorFormSet = modelformset_factory(Author, fields = ('__all__'),extra=3)              ##multiple form
    formset = AuthorFormSet

    # Add the formset to context dictionary
    context['formset'] = formset
    return render(request, 'formss/author_formset.html', context)


'''model form factoroy to made different form '''


# def time_date(request):
#     context={}
#     TimeDateFormSet = modelformset_factory(TimeDate,fields=('__all__'))
#     formset = TimeDateFormSet()
#
#     context['formset'] = formset
#     return render(request,'formss/time_date.html', context)


def time_date(request):
    if request.method == 'POST':
        surname = request.POST['surname']
        time_now = request.POST['time_now']
        detail = TimeDate.objects.create(surname=surname, time_now=time_now)
        return redirect('date_formatshow')
    else:
        form = TimeDateForm()
    return render(request, 'formss/time_date.html', {"form": form})


def date_formatshow(request):
    mydata = TimeDate.objects.all().values()
    context = mydata
    return render(request, 'formss/date_formatshow.html', {"context": context})
