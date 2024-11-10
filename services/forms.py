from django import forms

from users.models import Company
from .models import Service, Service_request


class CreateNewService(forms.ModelForm):
    name = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, label="Description")
    price_hour = forms.DecimalField(decimal_places=2, max_digits=5, min_value=0.00)
    field = forms.ChoiceField(required=True, choices=Service.choices)

    def __init__(self, *args, **kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)
        # adding placeholders to form fields
        self.fields["name"].widget.attrs["placeholder"] = "Enter Service Name"
        self.fields["description"].widget.attrs["placeholder"] = "Enter Description"
        self.fields["price_hour"].widget.attrs["placeholder"] = "Enter Price per Hour"

        self.fields["name"].widget.attrs["autocomplete"] = "off"

    class Meta:
        model = Service
        fields = ["name", "description", "price_hour", "field"]


class RequestServiceForm(forms.Form):
    address = forms.CharField(
        max_length=100,
        label="Address",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your physical address",
            }
        ),
        help_text="Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.",
    )
    service_time = forms.TimeField(
        widget=forms.TimeInput(
            format="%H:%M", attrs={"class": "form-control", "placeholder": "HH:MM"}
        ),
        label="Service Time",
        input_formats=["%H:%M"],
        help_text="Input desired service time interval",
    )
