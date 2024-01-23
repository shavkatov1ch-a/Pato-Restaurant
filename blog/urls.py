from django.urls import path
from .views import home, pato, menu

urlpatterns = [
    path('', home, name='home'),
    path('pato/', pato, name='pato'),
    path('menu/', menu, name='menu')

]