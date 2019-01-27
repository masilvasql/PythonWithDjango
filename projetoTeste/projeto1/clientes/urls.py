from django.urls import path
from .views import personList


urlpatterns = [
    path('list/', personList),
]
