from django.db import models
from django.urls import reverse
from datetime import datetime 
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.

#S.T. created Book Details model below
class Book(models.Model):
    book_name = models.CharField(max_length = 256)
    description = models.CharField(max_length=10000)
    genre = models.CharField(max_length = 256)
    cover = models.ImageField(null=True, upload_to='media')
    publishing_info = models.CharField(max_length = 256)
    published_date = models.DateField(default=datetime.now) 
    author = models.CharField(max_length = 256, default = "Author Unkown")
    author_bio = models.CharField(max_length=10000, default = "N/A")
    price = models.IntegerField(default=10)

    #average_rating
    class Meta:
      verbose_name_plural = "Books"

    def __str__(self):
        return str(self.book_name)
    
    def get_absolute_url(self):
        return reverse('bookDetails', args=[self.book_name])

#C.S. created models relating to Shopping Cart below
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
      return self.user.username


class OrderItem(models.Model):
    product = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    quantity = models.IntegerField(default = 1, validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.product.book_name

    def get_total_item_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.get_total_item_price()
        return total