from django.urls import path
from . import views
from .views import CarCreate, CarDelete

urlpatterns = [
    path('create/', views.CarCreate.as_view(), name='car-create'),
    path('delete/<int:car_id>/', views.CarDelete.as_view(), name='car-delete'),
    path('car-list/', views.car_list, name='car-list'),
]

 