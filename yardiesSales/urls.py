from django.urls import path
from .views import CreateSaleLocationView



urlpatterns = [
    path('create/', CreateSaleLocationView.as_view, namespace='yardiesSales'),
]