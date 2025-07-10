from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:item_id>/', views.delete_food, name='delete_food'),
    path('reset/', views.reset_day, name='reset_day'),
]
