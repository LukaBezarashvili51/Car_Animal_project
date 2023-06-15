from django.urls import path
from . import views
from .views import AnimalCreate, AnimalDelete

urlpatterns = [
    path('create/', views.AnimalCreate.as_view(), name='animal-create'),
    path('delete/<int:animal_id>/', views.AnimalDelete.as_view(), name='Animal-delete'),
    path('animal-list/', views.animal_list, name='animal-list'),
]


