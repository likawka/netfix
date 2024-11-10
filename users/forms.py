from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
from services.models import Service


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerSignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your name",
            }
        ),
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Email"})
    )

    birth = forms.DateField(widget=DateInput(), help_text="Enter your birth date")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")


class CompanySignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your name",
            }
        ),
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Email"})
    )

    field = forms.ChoiceField(choices=Service.choices, help_text="Choose field of work")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email", widget=forms.TextInput(attrs={"placeholder": "Enter Email"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}),
    )
