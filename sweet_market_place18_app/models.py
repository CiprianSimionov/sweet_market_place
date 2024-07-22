from django.db import models

# Create your models here.
#vom defini structura bazei de date
#vom instala libraria Pillow folosind comanda python -m pip install Pillow
#este pentru a manipula si prelucra imaginile. Poate fi folosita pentru a salva imagini in diferite formate(png,jpg)

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



