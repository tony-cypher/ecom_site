from django.db import models

# Create your models here :
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Order(models.Model):
    item = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=20)
    total = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} from {self.city}'