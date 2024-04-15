from django.contrib import admin
from django.urls import path
from driver import views

urlpatterns = [
    path("home/",views.HomePage.as_view(),name="home_3"),
    path("request/",views.CollectionRequestView.as_view(),name="rqst"),
    
    
]
