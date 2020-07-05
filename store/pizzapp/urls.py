from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('impressum/', views.impressum, name='impressum'),
    path('success/', views.success, name='success'),
    path('menu/', views.PizzaView.as_view(), name='menu'),
    path('menu/<slug:slug>/', views.detail, name='menu-detail'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
]
