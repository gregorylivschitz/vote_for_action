
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from vote_in_action.forms import VoteInActionAuthenticationForm


urlpatterns = [
    url(r'^activate/complete/$',
        TemplateView.as_view(template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^activate/(?P<activation_key>\w+)/$',
        ActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/$',
        RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register'),
    url(r'^register/complete/$',
        TemplateView.as_view(template_name='registration/registration_complete.html'),
        name='registration_complete'),
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'registration/login.html'},
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'registration/logout.html',
          'authentication_form': VoteInActionAuthenticationForm},
        name='logout'),
    url(r'^password/change/$',
        auth_views.password_change,
        name='password_change'),
    url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),
    url(r'^password/reset/$',
        auth_views.password_reset,
        name='password_reset'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),
]
