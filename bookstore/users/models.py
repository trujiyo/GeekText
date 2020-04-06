from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    pass
        # Add additional fields in here
        #first_name = form.models.CharField(_("First Name"), max_length=50)
        #last_name = form.models.CharField(_("Last Name"), max_length=50)
        #address = form.models.models.GenericIPAddressField(_(""), protocol="both", unpack_ipv4=False)

    def __str__(self):
        return self.username