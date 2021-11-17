from django.shortcuts import render, get_object_or_404
from .models import Book, ArtsAndCraft, Game

# Create your views here.

def all_books(request):
    """ A view to show all products """

    products = Book.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def all_arts_and_crafts(request):
    """ A view to show all products """

    products = ArtsAndCraft.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/artsandcraft.html', context)


def all_games(request):
    """ A view to show all products """

    products = Game.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/games.html', context)


def product_detail(request, product_id):
    """ A view to show individual book details """

    product = get_object_or_404(Book, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

