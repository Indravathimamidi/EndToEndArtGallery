# myproject/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import upload_Product, Product_list, home, explore, arts, crafts, productView, addToCart, cartView

urlpatterns = [
    # myapp/urls.py
    path('', home, name='home'),
    path('upload/', upload_Product, name='upload_Product'),
    path('Products/', Product_list, name='Product_list'),
    path('home/', home, name='home'),
    path('explore/', explore, name='explore'),
    path('arts/', arts, name='arts'),
    path('crafts/', crafts, name='crafts'),
    path('product/<int:id>/', productView, name='productView'),
    path('add-to-cart/<int:product_id>/', addToCart, name='addToCart'),
    path('cart/', cartView, name='cartView'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
