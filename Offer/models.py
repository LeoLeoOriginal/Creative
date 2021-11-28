from django.db import models

# Create your models here.
class Order(models.Model):
    order_serial = models.IntegerField(primary_key=True, unique=True, )
    name = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    style = models.CharField(max_length=10)
    details = models.TextField(max_length=1000000)
    
    def __str__(self):
        return self.order_serial