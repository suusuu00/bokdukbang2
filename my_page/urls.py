from django.urls import path
from .views import *

app_name = "my_page"

urlpatterns = [
    path("my-interest/", MyInterestList.as_view(), name="my_interest_list")
]
