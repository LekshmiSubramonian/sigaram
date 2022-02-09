from django.urls import path
from data import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="about"),
    path('home/', views.home, name="home"),
    path('saleform/', views.saleform, name="saleform"),
    path('rentform/', views.rentform, name="rentform"),
    path('advertise/', views.advertise, name="advertise"),
    path('search/', views.search, name="search"),
    path('order/', views.order, name="order"),
    path('orderrent/', views.orderrent, name="orderrent"),
    path('thankyou/', views.thankyou, name="thankyou"),
]
