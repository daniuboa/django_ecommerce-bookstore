from importlib.resources import path
from django.urls import reverse

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
]