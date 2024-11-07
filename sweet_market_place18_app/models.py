from django.db import models

# Create your models here.
#Define database
#install Pillow library using command python -m pip install Pillow
#for manipulating images. Can be used to save images in different formats(png,jpg)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField(null=True)
    weight = models.PositiveIntegerField(default=0)
    available = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name



