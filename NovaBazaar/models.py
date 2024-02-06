from django.db import models

# Create your models here.
class Product(models.Model):
    ProductName = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Order = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ProductName
    
    

