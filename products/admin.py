from django.contrib import admin
from .models import Product, Category

# Register your models here.

# Makes the following fields display in admin
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'category',
        'format',
        'price',
        'book_depository_stars',
        'isbn',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
