from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book, ArtsAndCraft, Game, Category
from itertools import chain


# Create your views here.

# Search bar
def search(request):
    q = request.GET['search']

    products = Book.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    artsandcrafts = ArtsAndCraft.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    games = Game.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))

    context = {
        'products': products,
        'artsandcrafts': artsandcrafts,
        'games': games,
        'page_name': 'Search Results',
        'q': q
    }

    return render(request, "products/search_products.html", context)



def all_books(request):
    """ A view to show all products """

    products = Book.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def all_arts_and_crafts(request):
    """ A view to show all products """

    artsandcrafts = ArtsAndCraft.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            artsandcrafts = artsandcrafts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            artsandcrafts = artsandcrafts.filter(queries)

    context = {
        'artsandcrafts': artsandcrafts,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products_artsandcraft.html', context)


def all_games(request):
    """ A view to show all products """

    games = Game.objects.all()

    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            games = games.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            games = games.filter(queries)

    context = {
        'games': games,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products_games.html', context)


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

