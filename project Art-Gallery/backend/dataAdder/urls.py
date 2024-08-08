# myproject/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import upload_image, image_list, home, explore, arts, crafts, productView

urlpatterns = [
    # myapp/urls.py
    path('upload/', upload_image, name='upload_image'),
    path('images/', image_list, name='image_list'),
    path('home/', home, name='home'),
    path('explore/', explore, name='explore'),
    path('arts/', arts, name='arts'),
    path('crafts/', crafts, name='crafts'),
    path('product/<int:id>/', productView, name='productView'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
