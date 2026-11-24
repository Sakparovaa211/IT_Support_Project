
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('create/', views.ticket_create, name='ticket_create'),
    path('delete/<int:pk>/', views.ticket_delete, name='ticket_delete'),
]
