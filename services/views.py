from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from users.models import Company, Customer, User

from .models import Service, Service_request
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    services = list(services)
    for serv in services:
        serv.times_requested = len(Service_request.objects.filter(service=serv))
    services.sort(key=lambda serv: serv.times_requested, reverse=True)

    return render(request, "services/list.html", {"services": services})


def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, "services/single_service.html", {"service": service})


def create(request):
    if request.method == "POST":
        form = CreateNewService(request.POST)
        if form.is_valid():
            # Perform additional logic or save the data to the database
            service = form.save(commit=False)
            service.user = request.user
            service.company = request.user.company
            service.save()

            # Redirect or show a success message
            return redirect("/services")
    else:
        form = CreateNewService()

    return render(request, "services/create.html", {"form": form})


def service_field(request, field):
    # search for the service present in the url
    field = field.replace("-", " ").title()
    services = Service.objects.filter(field=field)
    return render(
        request, "services/field.html", {"services": services, "field": field}
    )


def request_service(request, id):
    if request.method == "POST":
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service = Service_request(
                service=Service.objects.get(id=id),
                user=User.objects.get(email=request.user.email),
                address=form.cleaned_data["address"],
                service_time=form.cleaned_data["service_time"],
            )
            service.save()
            return redirect(f"/customer/{request.user.username}")
    else:
        form = RequestServiceForm()

    return render(request, "services/request_service.html", {"form": form})
