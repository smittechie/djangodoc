from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template


# Create your views here.
def templateapi(request):
    # template = Template("My name is {{ my_name }}.")
    # context = Context({"my_name": "Dolores"})
    # return render(request, 'templateapi/index.html', {'context': template.render(context)})

    t = Template("My name is {{ person.first_name }}.")
    d = {"person": {"first_name": "Joe", "last_name": "Johnson"}}
    return render(request, 'templateapi/index.html', {'context': t.render(Context(d))})
