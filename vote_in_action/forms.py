from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Submit, Layout
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from vote_in_action.models import RegistrationVoteUser


class VoteInActionAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or email address",
        max_length=254
    )

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        if username_or_email and '@' in username_or_email:
            users = User.objects.filter(email=username_or_email)
            if len(users) == 1:
                self.cleaned_data['username'] = users[0].username
        super(VoteInActionAuthenticationForm, self).clean()

class RegistrationVoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationVoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            'street_address',
            'street_address2',
            'city',
            'state',
            'home_phone')
        self.helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model = RegistrationVoteUser
        fields = ("street_address", "street_address2", "city", "state", "home_phone")
        labels = {
            'street_address': 'What is your address?',
        }

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            'favorite_food',
            'favorite_color',
            'favorite_number',)
        self.helper.add_input(Submit('submit', 'Submit'))
