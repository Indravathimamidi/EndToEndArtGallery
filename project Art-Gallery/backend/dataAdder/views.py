from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
# Create your views here.
# myapp/views.py

from .models import Product
from .forms import ProductForm


def upload_Product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Product_list')
    else:
        form = ProductForm()
    return render(request, 'upload.html', {'form': form})

def Product_list(request):
    Products = Product.objects.all()
    return render(request, 'ProductList.html', {'Products': Products})

def home(request):
    return render(request, 'index.html');

def explore(request):
    return render(request,  'explore.html');

def arts(request):
    # Filter Products by category 'arts'
    arts_Products = Product.objects.filter(category='art')
    return render(request, 'products.html', {'items': arts_Products})


def crafts(request):
    # Filter Products by category 'crafts'
    crafts_Products = Product.objects.filter(category='craft')
    return render(request, 'products.html', {'items': crafts_Products})

def productView(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'productView.html', {'product': product})

cart ={}
def addToCart(request, product_id):
    product = Product.objects.filter(id=product_id)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    print(cart)
    print(product)
    # request.session['cart'] = cart
    # return JsonResponse({'success': True, 'product_id': product_id, 'quantity': cart[product_id]})
    return render(request, 'cart.html', {'cart':cart, 'product':product})

def cartView(request):
    # cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    return render(request, 'cart.html', {'products': products, 'cart': cart})

