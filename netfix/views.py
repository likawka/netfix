from django.shortcuts import render

from users.models import User, Company
from services.models import Service, Service_request


def customer_profile(request, name):
    user = User.objects.get(username=name)
    service_requests = Service_request.objects.filter(user_id=user.id).order_by("-id")
    for req in service_requests:
        req.total_price = round(
            float(req.service.price_hour)
            * (req.service_time.hour + req.service_time.minute / 60),
            2,
        )
    return render(
        request,
        "users/profile.html",
        {"user": user, "service_requests": service_requests},
    )


def company_profile(request, name):
    # fetches the company user and all of the services available by it
    user = User.objects.get(username=name)
    services = Service.objects.filter(company=Company.objects.get(user=user)).order_by(
        "-date"
    )

    return render(request, "users/profile.html", {"user": user, "services": services})
