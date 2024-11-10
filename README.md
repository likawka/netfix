# Netfix

Netfix is a platform for limited field of service offerings.

You can register either as a company or a customer.

- Company can create service offering, set it's name, description, price and field of service.

* Customer can request such a service if it's already created.

  - When requesting a service, customer has to fill in a short form with his address and a period of time he needs service for.

* Both company and customer can view their profile. It shows their respective info.
  - For customer it's name, date of birth, email, user type and previous requested services.
  - For company it's name, email, user type (with field of work in front) and available services (services that this company provides).

# Running project

This project is built with Django and requires several dependencies to run. Follow the steps below to set up your local environment and run the project.

## Prerequisites

    Mini-Conda: Install Mini-Conda by following the instructions provided at https://docs.conda.io/en/latest/miniconda.html.

## Setup Instructions

```
# Create a Conda environment and install the required dependencies
conda create --name <name> python=3.8 Django=4.1

# Activate the Conda environment
conda activate <name>

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver

```

## Audit

Go to http://localhost:8000.
