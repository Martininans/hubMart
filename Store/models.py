from django.db import models
from django.conf import settings


# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collections = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion = models.ManyToManyField('Promotion', related_name='+')


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    PAYMENT_STATUS = [
        ('P', 'Pending'),
        ('S', 'Success'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default='P')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Promotion(models.Model):
    product = models.ManyToManyField("Product", related_name='+')
    discount = models.DecimalField(max_digits=6, decimal_places=2)


    
    def __str__(self):
        return f"{self.title} {self.price}"
