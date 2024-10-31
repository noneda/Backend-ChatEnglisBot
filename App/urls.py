from django.urls import path
from .views import *

urlpatterns = [
    path('', rootData),
    path('Bot/', botMessage)
]
