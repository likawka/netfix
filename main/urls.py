from django.urls import path
from . import views as v
from users.views import LoginUserView

app_name = "main"

urlpatterns = [
    path('', v.home, name='home'),
    path('logout/', v.logout, name='logout'),
    path('login/', LoginUserView, name='login_user'),
]
