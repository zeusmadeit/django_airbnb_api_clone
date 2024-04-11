from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=40)
    property_type = models.CharField(blank=False)
    total_bedrooms = models.CharField(blank=False)
    total_bathrooms = models.CharField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(blank=False)
    address = models.CharField(blank=False)
    price = models.IntegerField(blank=False)
    created_at = models.DateTimeField(blank=False)
    updated_at = models.DateTimeField(blank=False)
    published_at = models.DateTimeField(blank=False)

    def __str__(self):
        return self.name