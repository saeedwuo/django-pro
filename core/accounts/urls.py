from django.urls import path
from . import views 


app_name ="acc"

urlpatterns = [
    path('acc/',views.APIAcclist.as_view(),name="acc-list")
]