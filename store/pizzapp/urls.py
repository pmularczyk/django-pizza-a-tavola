from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('menu/', views.PizzaView.as_view(), name='menu')
]
