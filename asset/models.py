from django.db import models
from django.contrib.auth.models import User

# Data for dashboard

class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    artist = models.CharField(max_length=200, blank=True, null=True)
    dimension = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='artworks/', blank=True)  # this will store the image in a folder named 'artworks'
    purchase_date = models.DateField()
    #if we delete user, we delete the assets tied to them too
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    #fix plural name in admin portal
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name