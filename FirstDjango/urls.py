from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.items_list, name='items_list'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('about/', views.about, name='about'),
]