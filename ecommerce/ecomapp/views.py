from django.shortcuts import render
from .models import Order, Item, OrderItem


# Create your views here.
def item_list(request):
    context={
        'items':Item.objects.all()
    }
    return render(request, 'home-page.html', context)