from django.urls import path
from shipping.views import create_shipping, allShipping
urlpatterns = [
    path('create/', create_shipping),
    path('shippings/', allShipping)
    
   
]
