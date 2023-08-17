from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('', home, name="home"),
    path('in1/', index, name="index"),
    path('in2/', index1, name="index1"),
    path('admin/', admin.site.urls),
]
