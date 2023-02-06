from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import NameForm, ContactForm, AuthorForm


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
