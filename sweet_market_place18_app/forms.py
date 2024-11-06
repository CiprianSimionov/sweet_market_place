from django import forms
from .models import Product

#create here all clases needed for custom(default) forms

class ProductForm(forms.ModelForm):
    class Meta: #clasa care ajuta sa modelam formularul din upload_product
        model = Product #facem referire la formularul pentru produs
        fields = [ #fieldurile echivalent cu coloanele din baza de date
            "name", "description", "price", "ingredients", "weight", "available", "image"
        ]