from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#To call a view you need to map it to a URL, this is where you put your URLConfigs
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:title>', views.bookDetails, name='bookDetails'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)