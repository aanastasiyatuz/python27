from django.db import models

class Product(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title