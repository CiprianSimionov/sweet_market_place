#here we define roots for the application: sweet_market_place18

from django.urls import path
from sweet_market_place18_app.views import home_view, product_upload, ProductListView, product_details



app_name = 'sweet_market_place18_app'
urlpatterns = [
    path('', home_view, name="home"),
    path('upload_product/', product_upload, name="product_upload"),
    path('products/', ProductListView.as_view(), name="products"),
    path('product/<int:product_id>/', product_details, name="product"),
]
