from django.urls import path
from .views import personList
from .views import personNew
from .views import personUpdate

urlpatterns = [
    path('list/', personList, name = 'personList'),
    path('new/', personNew, name = 'personNew'),
    path('update/<int:id>/', personUpdate, name ='personUpdate')
]
