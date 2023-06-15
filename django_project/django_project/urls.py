from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', include('Car.urls')),
    path('admin/', admin.site.urls),
    path('Car/', include('Car.urls')),
    path('animal/', include('Animal.urls')),
]

