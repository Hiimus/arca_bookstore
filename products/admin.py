from django.contrib import admin
from .models import Book, ArtsAndCraft, Game, Category

# Register your models here.

# Makes the following fields display in admin
class BookAdmin(admin.ModelAdmin):
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

class ArtsAndCraftAdmin(admin.ModelAdmin):
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

class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(ArtsAndCraft, ArtsAndCraftAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)
