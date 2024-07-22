from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.views.generic import ListView



# Create your views here.

def home_view(request):
    return render(request, 'sweet_market_place18_app/home.html')

#este o functie cu ajutorul careia putem sa incarcam produse folosind un sablon, upload_product
def product_upload(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProductForm()
    return render(request, template_name='sweet_market_place18_app/upload_product.html', context={
        "form": form
    })

class ProductListView(ListView): #cream si afisam o lista de produse/obiecte
    model = Product
    template_name = 'sweet_market_place18_app/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = context["object_list"]
        return context

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, template_name='sweet_market_place18_app/product.html', context={
        "product": product
    })

