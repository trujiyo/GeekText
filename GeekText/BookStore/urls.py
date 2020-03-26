from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#To call a view you need to map it to a URL, this is where you put your URLConfigs
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:title>', views.bookDetails, name='bookDetails'),
    #C.S. Urls
    path('add_to_cart/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('order_summary/', views.order_details, name='order_summary'),
    path('item/delete/<item_id>', views.delete_from_cart, name='delete_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-quantity-from-cart/<item_id>', views.add_quantity_from_cart, name='add_quantity_from_cart'),
    path('reduce-quantity-from-cart/<item_id>', views.reduce_quantity_from_cart, name='reduce_quantity_from_cart'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)