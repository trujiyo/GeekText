from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class CustomUser(AbstractUser):
    pass
        # Add additional fields in here
        #first_name = form.models.CharField(_("First Name"), max_length=50)
        #last_name = form.models.CharField(_("Last Name"), max_length=50)
        #address = form.models.models.GenericIPAddressField(_(""), protocol="both", unpack_ipv4=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    user_profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)