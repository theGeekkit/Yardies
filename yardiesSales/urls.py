from django.urls import path
from . import views

app_name = 'yardiesSales'

urlpatterns = [
    path('sale/', views.SaleLocation.as_view(), namespace='Sales'),
]