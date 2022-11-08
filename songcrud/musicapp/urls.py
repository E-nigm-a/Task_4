# from django.contrib import admin
# from django.urls import path

# from . import views

# urlpatterns = [
#     path('index/', views.index, name='index')
# ]

from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'songs', SongViewSet, basename='songs')

urlpatterns = [] + router.urls