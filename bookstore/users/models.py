from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.

# class CustomUser(AbstractUser):
#     pass
#         # Add additional fields in here
#         #first_name = form.models.CharField(_("First Name"), max_length=50)
#         #last_name = form.models.CharField(_("Last Name"), max_length=50)
#         #address = form.models.models.GenericIPAddressField(_(""), protocol="both", unpack_ipv4=False)

#     def __str__(self):
#         return self.username

from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # def delete_user(self):
    #     self.user.delete()