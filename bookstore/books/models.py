from django.db import models
from django.urls import reverse
from datetime import datetime 
from django.conf import settings
from django.core.validators import MinValueValidator


STATUS_CHOICES=(
    (1, '1'),
    (2, '2'),
    (3,'3'),
    (4, '4'),
    (5, '5'),
)
        
# Create your models here.
class Genre(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(max_length=200, db_index=True)
   

    class Meta:
        ordering = ('name',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(null= True, max_length=10000)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)

#S.T. started Book Details model below
class Book(models.Model):
    """Model class for books"""

    book_name = models.CharField(max_length = 256)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=10000)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    cover = models.ImageField(null=True, upload_to='media')
    #we're assuming that no book is published before 0 A.D.
    published_date = models.DateField(null=True, blank=True)
    publishing_info = models.CharField(max_length = 256)
    price = models.DecimalField(null = True, max_digits=10, decimal_places=2)
    top_seller = models.BooleanField(default=False)
    rating = models.IntegerField(choices=STATUS_CHOICES, default=1)


    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    class Meta:
      ordering = ['book_name']
      verbose_name_plural = "Books"
      

    def __str__(self):
        return str(self.book_name)
    
    def get_absolute_url(self):
        return reverse('bookDetails', args=[self.book_name])


# #C.S. created models relating to Shopping Cart below
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#       return self.user.username
 

class OrderItem(models.Model):
    product = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    quantity = models.IntegerField(default = 1, validators=[MinValueValidator(1)])
    is_saved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product.book_name

    def get_total_item_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey('users.Profile', on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        book = self.items.filter(is_saved = False)
        return book

    def get_save_items(self):
        book = self.items.filter(is_saved = True)
        return book

    def get_total_price(self):
        total = 0
        for item in self.items.filter(is_saved = False):
            total += item.get_total_item_price()
        return total

    def get_total_save_price(self):
        total = 0
        for item in self.items.filter(is_saved = True):
            total += item.get_total_item_price()
        return total

