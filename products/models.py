from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories' # Fixes spelling error in admin


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
    author = models.CharField(max_length=260, null=True, blank=True)
    format = models.CharField(max_length=260, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=260)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    isbn = models.BigIntegerField(null=True, blank=True)
    img_paths = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    new_rating = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
