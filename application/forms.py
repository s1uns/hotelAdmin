from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': ''
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': ''
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': '',
        }))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': '',
        }))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password',
            'class': '',
        }))

class OrderPremiseForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    check_in_date = forms.DateField(label='Check-In Date')
    check_out_date = forms.DateField(label='Check-Out Date')

    def __init__(self, *args, **kwargs):
        premise_choices = kwargs.pop('premise_choices')
        super(OrderPremiseForm, self).__init__(*args, **kwargs)
        self.fields['premise'] = forms.ChoiceField(choices=premise_choices, label='Select Premise')
