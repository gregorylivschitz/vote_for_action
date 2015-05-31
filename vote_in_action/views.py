from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.contrib.auth.models import User
from vote_in_action.forms import ExampleForm
from vote_in_action.models import Bills

# Create your views here.


def index(request):
    template = Template('index.html')
    bills = Bills.objects.all()
    context = ({'bills': bills})
    # return template.render(context)
    return render(request, 'index.html', context)

def vote_example(request):
    context = ({'example_form': ExampleForm})
    return render(request, 'example.html', context)