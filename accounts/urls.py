from django.urls import path
from .views import *

urlpatterns = [
    path("register/",resgister_view),
    path("login/",login_view),
    path("refresh/",refresh_token_view),
    path("logout/",logout_view)
]
