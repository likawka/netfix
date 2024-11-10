from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView

from .forms import CustomerSignUpForm, CompanySignUpForm, UserLoginForm
from .models import User, Company, Customer


def register(request):
    return render(request, "users/register.html")


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = "users/register_customer.html"

    def form_valid(self, form):
        form.instance.is_customer = True
        user = form.save()
        customer = Customer.objects.create(user=user, birth=form.cleaned_data["birth"])
        customer.save()
        login(self.request, user)
        return redirect("/")


class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = "users/register_company.html"

    def form_valid(self, form):
        form.instance.is_company = True
        user = form.save()
        company = Company.objects.create(user=user, field=form.cleaned_data["field"])
        company.save()
        login(self.request, user)
        return redirect("/")


def LoginUserView(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_company:
                    company = Company.objects.get(user=user)
                    company.save()
                if user.is_customer:
                    customer = Customer.objects.filter(user=user).first()
                    customer.save()
                return redirect("/")
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = UserLoginForm()

    return render(request, "users/login.html", {"form": form})
