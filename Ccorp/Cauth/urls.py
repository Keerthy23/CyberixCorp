from django.urls import path
from Cauth import views

urlpatterns = [
    path('',views.Home,name="Home")
]