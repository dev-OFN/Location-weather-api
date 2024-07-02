from django.urls import path
from .views import Helloapi

urlpatterns = [
    path('api/hello',Helloapi.as_view(), name='hello'),
]
