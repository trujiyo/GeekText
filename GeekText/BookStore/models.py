from django.db import models
from django.urls import reverse
from datetime import datetime 

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
    #average_rating
    class Meta:
      verbose_name_plural = "Books"

    def __str__(self):
        return str(self.book_name)
    
    def get_absolute_url(self):
        return reverse('bookDetails', args=[self.book_name])