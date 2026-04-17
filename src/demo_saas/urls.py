
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("",base_page, name='base'),
    path("home/",home_page, name='home_pg'),
    # path("about/",about_page, name='about')
]
