from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    Books = Book.objects.all()
    return render(request, 'BookDetails/index.html', {'Book': Books})    

def bookDetails(request, title):
    book = Book.objects.filter(book_name=title)
    return render(request, 'BookDetails/bookDetails.html', {'Book': book}) 