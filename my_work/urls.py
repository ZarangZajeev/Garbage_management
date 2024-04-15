from django.contrib import admin
from django.urls import path
from my_work import views

urlpatterns = [
    path("home/",views.HomePage.as_view(),name="home_1"),
    path("add/",views.AddUser.as_view(),name="add"),
    # path("userlocation/",views.UserLocationView.as_view(),name="user_location"),
    path("createbin/",views.CreateGarbage.as_view(),name="create_garbage"),
    path("updatebin/<int:pk>",views.UpdateBin.as_view(),name="update_garbage"),
    path("deletebin/<int:pk>",views.DeleteBin.as_view(),name="delete_garbage"),
    path("publiclist/",views.UsersList.as_view(),name="userlist"),
    path("driverlist/",views.DriverList.as_view(),name="driver_list"),
    path("complaintlist/",views.ComplaintView.as_view(),name="compliantlist"),
    path("Addarea/",views.AddLocation.as_view(),name="area"),
    path("logout/",views.Signout.as_view(),name="lgout") ,
    path("login",views.CustomLoginView.as_view(),name="lgn")
  

]