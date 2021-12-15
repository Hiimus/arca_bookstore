from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.

# Makes the following fields display in admin
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'category',
        'format',
        'price',
        'rating',
        'isbn',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
        'created_at',

    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
