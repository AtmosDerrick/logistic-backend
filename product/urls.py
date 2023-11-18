from django.urls import path
from product.views import create_product,product_list


urlpatterns = [
    path('create/', create_product ),
    path('products/', product_list)
   
]
