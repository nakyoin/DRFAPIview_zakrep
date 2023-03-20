from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default='Неизвестно')
    price = models.CharField(max_length=255)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=True, related_name='cartprod')
    descript = models.ManyToManyField(Product)
    allprice = models.IntegerField(max_length=10, default=0, null=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return str(self.product)