from django.urls import path
from . import views

#To call a view you need to map it to a URL, this is where you put your URLConfigs
urlpatterns = [
    path('', views.index, name='index'),
    path('bookDetails/', views.bookDetails, name='bookDetails'),
    path('bookDetails/<str:title>', views.bookDetails, name='bookDetails'),
]