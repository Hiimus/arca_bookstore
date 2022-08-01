from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from profiles.models import UserProfile
from .forms import ProductForm, ReviewForm

import random


# Create your views here.

# Search bar
def search(request):

    products = Product.objects.all()
    query = None

    if 'search' in request.GET:
        query = request.GET['search']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, "products/products.html", context)


def all_products(request):
    """ Home page with a randomized sample of products """
    # Code inspired by:
    # https://stackoverflow.com/questions/22816704/django-get-a-random-object/23755881#23755881
    # Get objects by categories
    book_1 = list(Product.objects.filter(category=1))
    book_2 = list(Product.objects.filter(category=2))
    book_3 = list(Product.objects.filter(category=3))
    book_4 = list(Product.objects.filter(category=4))

    arts_and_craft_1 = list(Product.objects.filter(category=11))
    arts_and_craft_2 = list(Product.objects.filter(category=12))
    arts_and_craft_3 = list(Product.objects.filter(category=13))
    arts_and_craft_4 = list(Product.objects.filter(category=12))

    game_1 = list(Product.objects.filter(category=14))
    game_2 = list(Product.objects.filter(category=15))
    game_3 = list(Product.objects.filter(category=14))
    game_4 = list(Product.objects.filter(category=15))

    # Get a random sample
    # change 1 to how many random items you want
    books_1 = random.sample(book_1, 1)
    books_2 = random.sample(book_2, 1)
    books_3 = random.sample(book_3, 1)
    books_4 = random.sample(book_4, 1)

    arts_and_crafts_1 = random.sample(arts_and_craft_1, 1)
    arts_and_crafts_2 = random.sample(arts_and_craft_2, 1)
    arts_and_crafts_3 = random.sample(arts_and_craft_3, 1)
    arts_and_crafts_4 = random.sample(arts_and_craft_4, 1)

    games_1 = random.sample(game_1, 1)
    games_2 = random.sample(game_2, 1)
    games_3 = random.sample(game_3, 1)
    games_4 = random.sample(game_4, 1)

    context = {
        'books_1': books_1,
        'books_2': books_2,
        'books_3': books_3,
        'books_4': books_4,
        'arts_and_crafts_1': arts_and_crafts_1,
        'arts_and_crafts_2': arts_and_crafts_2,
        'arts_and_crafts_3': arts_and_crafts_3,
        'arts_and_crafts_4': arts_and_crafts_4,
        'games_1': games_1,
        'games_2': games_2,
        'games_3': games_3,
        'games_4': games_4,
    }

    return render(request, 'products/products_home.html', context)


def all_books(request):
    """ A view to show all Books, excludes arts & crafts and games """

    all_products = Product.objects.all()
    products = all_products.exclude(
        category=11).exclude(category=12).exclude(category=13).exclude(
            category=14).exclude(category=15)

    review = Review.objects.all()

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
        'review': review,
    }

    return render(request, 'products/products.html', context)


def all_arts_and_crafts(request):
    """ A view to show all Arts & Crafts """

    all_products = Product.objects.all()
    products = all_products.exclude(
        category=1).exclude(
            category=2).exclude(
                category=3).exclude(
                    category=4).exclude(
                        category=5).exclude(
                            category=6).exclude(
                                category=7).exclude(
                                    category=8).exclude(
                                        category=9).exclude(
                                            category=10).exclude(
                                                category=14).exclude(
                                                    category=15)

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

    return render(request, 'products/products.html', context)


def all_games(request):
    """ A view to show all games """

    all_products = Product.objects.all()
    products = all_products.exclude(
        category=1).exclude(
            category=2).exclude(
                category=3).exclude(
                    category=4).exclude(
                        category=5).exclude(
                            category=6).exclude(
                                category=7).exclude(
                                    category=8).exclude(
                                        category=9).exclude(
                                            category=10).exclude(
                                                category=11).exclude(
                                                    category=12).exclude(
                                                        category=13)

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

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    reviews = Review.objects.filter(product=product_id)
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(
        request, 'products/product_detail/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.info(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Add a review to a product """

    product = get_object_or_404(Product, pk=product_id)

    user = get_object_or_404(UserProfile, user=request.user)

    username = request.user.get_username()
    reviews = Review.objects.filter(product=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():

            review = form.save(commit=False)
            review.product = product
            review.user = user
            review.save()

            # Adds new rating to product
            number_of_ratings = product.ratings.all().count()
            all_ratings = []
            for rating in product.ratings.all():
                all_ratings.append(rating.rating)
            sum_rating = sum(all_ratings)
            new_rating = sum_rating / number_of_ratings
            product.rating = new_rating
            product.save()

            messages.info(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add review, \
                    please ensure the form is valid')
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
        'username': username,
    }

    return render(request, 'products/add_review.html', context)


@login_required
def delete_review(request, review_id):
    """ Delete a review to a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        review = Review.objects.all().filter(pk=review_id)
        review.delete()
        return redirect(reverse('all_products'))

    messages.success(request, 'Review deleted!')
    return render(request, 'delete_review.html')
    
    
