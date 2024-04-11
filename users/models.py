from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    phone_number = models.CharField()
    bio = models.CharField()
    user_type = models.CharField()
    profile_image = models.CharField()

    def __str__(self):
        return self.username