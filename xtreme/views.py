from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Category
from .models import Brand
from .models import Product
from .models import Cart, CartItem


# Create your views here.
def index(request):
    # Retrieve data from the database
    categories = Category.objects.all()
    brands = Brand.objects.all()

    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user).first()
        cart_items = CartItem.objects.filter(cart=cart)
        product_count = cart_items.count()
    else:
        product_count = 0
    # Limit the number of products and get the values
    products = Product.objects.all()[:8]

    context = {
        'products': products,
        'categories': categories,
        'brands': brands,
        'count': product_count,
    }

    return render(request, 'xtreme/index.html', context)

def product_details(request, id):
    """ Product details function """
    product = Product.objects.get(id=id)
    return render(request, 'xtreme/product_info.html', {'p': product})

@login_required
def add_to_cart(request):
    """ Add to cart function """
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        user_id = request.user.id

        cart, created = Cart.objects.get_or_create(user_id=user_id)
        if created:
            cart.cart_id = cart.id
            cart.save()

        try:
            product = Product.objects.get(id=product_id)
            cart_item = CartItem.objects.filter(product=product, cart=cart).first()

            if cart_item:
                response = {'exist': True, 'message': 'Item already exists in the cart'}
            else:
                cart_item = CartItem(product=product, cart=cart, quantity=quantity)
                cart_item.save()
                response = {'success': True, 'message': 'Item added to the cart successfully'}
        except Product.DoesNotExist:
            response = {'error': True, 'message': 'Product does not exist'}

        return JsonResponse(response)


def category_products(request, id):
    """ Category products function """
    category = Category.objects.get(id=id)
    products = category.product_set.all()  # This retrieves all products related to the category
    context = {
        'products': products,
        'name': category.name,
    }
    return render(request, 'xtreme/shop_listing.html', context)

def brand_products(request, id):
    """ Brand Products function """
    brand = Brand.objects.get(id=id)
    products = brand.products.all()
    brand_name = f"{brand.name} PCs"
    context = {
        'products': products,
        'name': brand_name,
    }
    return render(request, 'xtreme/shop_listing.html', context)

def contact_us(request):
    """ Contact us function """
    return render(request, 'xtreme/contact.html')

@login_required
def update_cart_item(request):
    """ Update cart function """
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        new_quantity = request.POST.get('new_quantity')

        # Implement logic to update your cart item using your models here

        response = {'message': 'Cart item updated successfully'}
        return JsonResponse(response)


def remove_cart(request):
    """ Remove cart function """
    if request.method == 'POST':
        product_id = request.POST.get('cart_item_id')
        user = request.user

        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.filter(cart=cart, product=product_id).first()
        if cart_item:
            cart_item.delete()
            messages.success(request, 'Item removed from the cart successfully!')
        else:
            messages.error(request, 'Item not found in the cart.')

        return JsonResponse({'success': True, 'message': 'successful', 'redirect': reverse('cart')})

@login_required
def cart(request):
    """ Cart function """
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    cart_items = CartItem.objects.filter(cart=cart)

    total_price = sum(item.product.price for item in cart_items)
    tax = 14
    discount = -12
    total_price_all = total_price + tax + discount
    product_count = cart_items.count()

    return render(request, 'xtreme/shopping_cart.html', {
        'products': cart_items,
        'total_price': total_price,
        'discount': discount,
        'tax': tax,
        'total_price_all': total_price_all,
        'count': product_count
    })

def register(request):
    """ Register function """
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['name'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f"Welcome {form.cleaned_data['name']}, Thank you for registering")
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form, 'title': 'Register'})

def login(request):
    """ Login function """
    if request.user.is_authenticated:
        return redirect('index')

    print("welcome")
    # Get the username and password from the POST request
    username = request.POST.get('username')
    password = request.POST.get('password')
    print('email: ', email, 'passwordd: ', password)
    user = User.objects.filter(email=email).first()
    if user and user.check_password(password):
        messages.success(request, f"Welcome back, {user.username}!")
        login(request, user)
        return redirect(request.GET.get('next', 'index'))
    else:
        messages.error(request, 'Invalid username or password')
    

    return render(request, 'login.html', {'form': form, 'title': 'Sign In'})

@login_required
def logout_view(request):
    """ Logout funtion """
    logout(request)
    return redirect('login')