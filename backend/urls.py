
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls') ),
    path('product/', include('product.urls') ),
    path('shipping/', include('shipping.urls') ),


]
