from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name="blogHome"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('tracker/', views.tracker,name="tracker"),
    path('search', views.search,name="search"),
    path('productView', views.productView,name="productView"),
    path('checkout', views.checkout,name="checkout"),
]