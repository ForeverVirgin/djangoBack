from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('<str:menu_name>/<path:categorypath>/', categories, name = "cat"),
    path('<str:menu_name>/',openmenu)
]