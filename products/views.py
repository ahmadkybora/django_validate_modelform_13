from django.shortcuts import render
from django.views.generic import CreateView

from .models import Product
from .forms import ProductForm

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create_product.html'
