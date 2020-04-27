from django.db import models
from django.conf import settings
from django.shortcuts import reverse


# Create your models here.
CATEGORY_CHOICES=(
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear'),
)

LABEL_CHOICES=(
    ('p', 'primary'),
    ('s', 'secondary'),
    ('d', 'danger'),
)

lorem_ipsum='Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
            Ut enim ad minim veniam, \quis nostrud exercitation ullamco laboris \
            nisi ut aliquip ex ea commodo consequat. \
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum \
            dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \
            sunt in culpa qui officia deserunt mollit anim id est laborum.'


class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True, null=True)
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label=models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug=models.SlugField()
    description=models.TextField(default=lorem_ipsum)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:product', kwargs={'slug':self.slug})

    def get_add_to_cart_url(self):
        return reverse('core:add_to_cart', kwargs={'slug':self.slug})

    def get_remove_from_cart_url(self):
        return reverse('core:remove_from_cart', kwargs={'slug':self.slug})


class OrderItem(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username