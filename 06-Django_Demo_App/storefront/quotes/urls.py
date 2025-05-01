from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/get-quote/', views.get_quote, name='get_quote'),
]