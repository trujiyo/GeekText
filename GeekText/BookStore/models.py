from django.db import models
from django.urls import reverse

# Create your models here.

#S.T. started Book Details model below
class Book(models.Model):
    book_name = models.CharField(max_length = 256)
    description = models.CharField(max_length=10000)
    genre = models.CharField(max_length = 256)
    publishing_info = models.CharField(max_length = 256)
    #average_rating
    #cover
    #author name and bio?
    class Meta:
      verbose_name_plural = "Books"

    def __str__(self):
        return str(self.book_name)
    
    def get_absolute_url(self):
        return reverse('bookDetails', args=[self.book_name])