from django.urls import path
from product.views import create_product,product_list,product_recieve,product_shipping,product_arrival


urlpatterns = [
    path('create/', create_product ),
    path('products/', product_list),
    path('recieveproduct/<location>/', product_recieve),
    path('shippingproduct/<location>/', product_shipping),
    path('arrivalproduct/<location>/', product_arrival)
    


   
]
