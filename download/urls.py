from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('', include('pictures.urls'))
]
