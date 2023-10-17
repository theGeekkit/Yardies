from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import SaleLocation
from .forms import CreateSaleLocationForm


class CreateSaleLocationView(CreateView):
    model = SaleLocation
    form = CreateSaleLocationForm
    name = "createsalelocation.html"
    success_url = reverse_lazy
    
    