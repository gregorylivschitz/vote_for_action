from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, Template
from django.contrib.auth.models import User
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from vote_in_action.forms import ExampleForm, RegistrationVoteForm, RegistrationFormUniqueEmailCrispy
from vote_in_action.models import Bills
import logging

# Create your views here.


def index(request):
    template = Template('index.html')
    bills = Bills.objects.all()
    context = ({'bills': bills})
    # return template.render(context)
    return render(request, 'index.html', context)

def vote_example(request):
    context = ({'example_form': RegistrationVoteForm})
    return render(request, 'example.html', context)


class VoteRegistrationView(RegistrationView):
    form_class = RegistrationFormUniqueEmailCrispy
    second_form_class = RegistrationVoteForm

    def get_context_data(self, **kwargs):
        context = super(VoteRegistrationView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def get(self, request, *args, **kwargs):
        super(VoteRegistrationView, self).get(request, *args, **kwargs)
        form = self.form_class
        form2 = self.second_form_class
        return self.render_to_response(self.get_context_data(form=form, form2=form2))

    def post(self, request, *args, **kwargs):
        #super(VoteRegistrationView, self).post(request, *args, **kwargs)
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            userdata = form.save()
            #userdata.save()
            registration_data = form2.save(commit=False)
            registration_data.user_id = userdata
            registration_data.save()
            return self.form_valid(request, form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form2=form2))
