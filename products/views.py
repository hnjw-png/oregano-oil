from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Image
from django.http import JsonResponse

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
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

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def product_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        product = Product(name=name, description=description)
        product.save()
        images = request.FILES.getlist('images')
        for image in images:
            img = Image(product=product, image=image)
            img.save()
    return render(request, 'product.html')


def images_by_product_name(request):
    if request.method == 'POST':
        product_name = request.POST.get('name')
        try:
            product = Product.objects.get(name=product_name)
            images = Image.objects.filter(product=product)
        except Product.DoesNotExist:
            images = None

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # AJAX request
            data = []
            for image in images:
                data.append({'url': image.image.url})
            return JsonResponse({'images': data})
    else:
        images = None
    return render(request, 'images.html', {'images': images})