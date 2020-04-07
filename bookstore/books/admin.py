from django.contrib import admin
from .models import Book, Genre, Author, Order, OrderItem
from django.apps import apps
#from users.models import Profile

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
   
admin.site.register(Genre, GenreAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'bio', 'date_of_birth',
                    'date_of_death']
   
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'author', 'description', 'genre',
                    'cover', 'published_date', 'publishing_info','price',
                    'top_seller', 'rating']
    list_filter = ['genre', 'top_seller', 'rating']
  
admin.site.register(Book, BookAdmin)


#admin.site.register(Profile) 
admin.site.register(Order) 
admin.site.register(OrderItem) 