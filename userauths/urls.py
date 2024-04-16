from django.urls import path
from userauths.views import (
    registerView,
    loginView,
    logoutView,
)

app_name = "userauths"

urlpatterns=[
    path('register/',registerView,name="register"),
    path('connexion/',loginView,name="connexion"),
    path('deconnexion/', logoutView,name="deconnexion")
]