from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm, ContactForm


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
