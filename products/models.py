from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=260)
    friendly_name = models.CharField(max_length=260, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.URLField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=260)
    author = models.CharField(max_length=260)
    format = models.CharField(max_length=260)
    book_depository_stars = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=260)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    isbn = models.IntegerField()
    img_paths = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
