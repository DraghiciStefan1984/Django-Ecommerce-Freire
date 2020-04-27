from django.shortcuts import get_object_or_404, redirect, render
from .models import Item, Order, OrderItem
from django.views.generic import ListView, DetailView
from django.utils import timezone


# Create your views here.
def item_list(request):
    context={'items':Item.objects.all()}
    return render(request, 'home-page.html', context)


def home(request):
    context={'items':Item.objects.all()}
    return render(request, 'home-page.html', context)


def checkout(request):
    return render(request, 'checkout.html', {})


def products(request):
    return render(request, 'product-page.html', {})


class HomeView(ListView):
    model=Item
    template_name='home.html'


class ItemDetailView(DetailView):
    model=Item
    template_name='product.html'


def add_to_cart(request, slug):
    item=get_object_or_404(Item, slug=slug)
    order_item=OrderItem.objects.create(item=item)
    order_queryset=Order.objects.filter(user=request.user, ordered=False)
    if order_queryset.exists():
        order=order_queryset[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity+=1
            order_item.save()
    else:
        ordered_date=timezone.now()
        order=Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect('core:product', slug=slug)