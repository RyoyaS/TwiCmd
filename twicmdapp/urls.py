from django.contrib import admin
from django.urls import path
from .views import twicmdfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('twicmd/',twicmdfunc, name='twicmd') 
]
