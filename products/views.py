from django.shortcuts import render, get_object_or_404
from .models import Book, ArtsAndCraft, Game

# Create your views here.

def all_books(request):
    """ A view to show all products """

    products = Book.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/books/products.html', context)


def all_arts_and_crafts(request):
    """ A view to show all products """

    artsandcrafts = ArtsAndCraft.objects.all()

    context = {
        'artsandcrafts': artsandcrafts,
    }

    return render(request, 'products/artsandcrafts/artsandcraft.html', context)


def all_games(request):
    """ A view to show all products """

    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'products/games/games.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    book = get_object_or_404(Book, pk=product_id)

    context = {
        'book': book,
    }

    return render(request, 'products/product_detail/product_detail.html', context)


def product_detail_arts(request, product_id):
    """ A view to show individual product details """

    artsandcraft = get_object_or_404(ArtsAndCraft, pk=product_id)

    context = {
        'artsandcraft': artsandcraft,
    }

    return render(request, 'products/product_detail/product_detail.html', context)


def product_detail_games(request, product_id):
    """ A view to show individual product details """

    game = get_object_or_404(Game, pk=product_id)

    context = {
        'game': game,
    }

    return render(request, 'products/product_detail/product_detail.html', context)

