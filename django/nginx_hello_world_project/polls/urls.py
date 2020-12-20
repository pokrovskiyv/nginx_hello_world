from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('hello/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('maxim/', views.hi_maxim, name='hi_maxim'),
    path('', views.task, name='')
]