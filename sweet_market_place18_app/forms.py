from django import forms
from .models import Product

#in cadrul acestui fisier vom crea toate clasele necesare pentru formulare personalizate

class ProductForm(forms.ModelForm):
    class Meta: #aceasta clasa ne ajuta sa modelam formularul din upload_product
        model = Product #facem referire la formularul pentru produs
        fields = [ #fieldurile echivalent cu coloanele din baza de date
            "name", "description", "price", "ingredients", "weight", "available", "image"
        ]