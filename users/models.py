from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    phone_number = models.CharField(max_length=15)
    bio = models.CharField(max_length=200)
    user_type = models.CharField(max_length=25)
    profile_image = models.CharField(max_length=80)

    def __str__(self):
        return self.username