from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
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
        'q': q,
        'result_count': products.count() + artsandcrafts.count() + games.count()
    }

    return render(request, "products/search_products.html", context)



def all_books(request):
    """ A view to show all Books """

    products = Book.objects.all()

    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products_books.html', context)


def all_arts_and_crafts(request):
    """ A view to show all Arts & Crafts """

    artsandcrafts = ArtsAndCraft.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                artsandcrafts = artsandcrafts.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            artsandcrafts = artsandcrafts.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            artsandcrafts = artsandcrafts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'artsandcrafts': artsandcrafts,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products_artsandcraft.html', context)


def all_games(request):
    """ A view to show all games """

    games = Game.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                games = games.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            games = games.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            games = games.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'games': games,
        'current_categories': categories,
        'current_sorting': current_sorting,
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

