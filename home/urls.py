from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('menu/', views.menu, name="menu_page"),
    path('order/table=<str:tableid>', views.orders, name="order_page"),
]