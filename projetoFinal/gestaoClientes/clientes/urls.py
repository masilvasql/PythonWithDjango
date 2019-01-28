from django.urls import path
from .views import personList
from .views import personNew
from .views import personUpdate
from .views import personDelete

urlpatterns = [
    path('list/', personList, name = 'personList'),
    path('new/', personNew, name = 'personNew'),
    path('update/<int:id>/', personUpdate, name ='personUpdate'),
    path('delete/<int:id>/', personDelete, name = 'personDelete')
]
