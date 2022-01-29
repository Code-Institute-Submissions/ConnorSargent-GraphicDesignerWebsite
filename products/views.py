from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg

from .models import Product, Category, ProductReview
from .forms import ProductForm, ProductReviewForm

# Create your views here.

def all_products(request):
    """ A view to show all products, sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',') #Split for multiple categories in one nav link
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Oops, Looks like you didn't enter anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)
    productreviews = ProductReview.objects.filter(product=product_id)

    average_rating = productreviews.aggregate(Avg("rating"))["rating__avg"]
    if average_rating is None:
        average_rating = 0
    average_rating = round(average_rating, 2)

    context = {
        'product': product,
        'productreviews': productreviews,
        "average_rating": average_rating
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add product """
    if not request.user.is_superuser:
        messages.error(request, 'Log in as an Admin to use this feature')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added succsessfully!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product """
    if not request.user.is_superuser:
        messages.error(request, 'Log in as an Admin to use this feature')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product successfully updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.')
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
    """ Delete a product """
    if not request.user.is_superuser:
        messages.error(request, 'Log in as an Admin to use this feature')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_product_review(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        if request.method == "POST":
            form = ProductReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.product = product
                data.save()
                return redirect("product_detail", product_id)
                messages.info(request, 'Review Added')
        else:
            form = ProductReviewForm()
        return render(request, 'product_detail.html', {"form": form})


@login_required
def edit_product_review(request, product_id, productreview_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        productreview = ProductReview.objects.get(product=product, id=productreview_id)

        if request.user == productreview.user or request.user.is_superuser:
            if request.method == "POST":
                form = ProductReviewForm(request.POST, instance=productreview)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 5) or (data.rating < 0):
                        error = "Out or range. Please select rating from 0 to 5."
                        return render(request, 'products/edit_product_review.html', {"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("product_detail", product_id)
                        messages.info(request, 'Review Edited')
            else:
                form = ProductReviewForm(instance=productreview)
                return render(request, 'products/edit_product_review.html', {"form": form})
        else:
            return redirect("product_detail", product_id)


@login_required
def delete_product_review(request, product_id, productreview_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        productreview = ProductReview.objects.get(product=product, id=productreview_id)

        if request.user == productreview.user or request.user.is_superuser:
            productreview.delete()
            messages.info(request, 'Review Deleted')

        return redirect("product_detail", product_id)
