from django.shortcuts import render
from .models import Item, Order, OrderItem


# Create your views here.
def item_list(request):
    context={'items':Item.objects.all()}
    return render(request, 'home-page.html', context)


def home(request):
    return render(request, 'home-page.html', {})


def checkout(request):
    return render(request, 'checkout-page.html', {})


def products(request):
    return render(request, 'product-page.html', {})