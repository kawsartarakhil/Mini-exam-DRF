from django.urls import path
from .views import *
urlpatterns = [
    path("loan_list/",get_loan_list),
    path("create/",create_loan),
    path("update/<int:pk>/",update_loan_view),
    path("delete/<int:pk>/",delete_loan),
    path("loan/<int:pk>/",get_loan)
]
