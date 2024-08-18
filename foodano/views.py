from django.shortcuts import render, redirect, get_object_or_404
from .models import Banner, Category, Product, ProductImg, ProductEnter, Cart, CartProduct, WishList, Order, Info
from django.contrib.auth.decorators import login_required
from .forms import BannerForm, CategoryForm, ProductForm, InfoForm, ProductEnterForm
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


def main(request):
    banners = Banner.objects.all()
    categories = Category.objects.all()
    info = Info.objects.all()
    return render(request, 'base.html', {'banners': banners, 'categories': categories, 'info': info})

# ==================================================================================



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    return render(request, 'registration/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('main')



def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'banner/banner_list.html', {'banners': banners})


def banner_detail(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    return render(request, 'banner/banner_detail.html', {'banner': banner})


@login_required
def banner_create(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            banner = form.save()
            return redirect('banner_detail', pk=banner.pk)
    else:
        form = BannerForm()
    return render(request, 'banner/banner_create.html', {'form': form})


@login_required
def banner_update(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            banner = form.save()
            return redirect('banner_detail', pk=banner.pk)
    else:
        form = BannerForm(instance=banner)
    return render(request, 'banner/banner_update.html', {'form': form})


@login_required
def banner_delete(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        banner.delete()
        return redirect('banner_list')
    return render(request, 'banner/banner_delete.html', {'banner': banner})

# ================================================================================

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()
    return render(request, 'category/category_detail.html', {'category': category, 'products': products})



@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'category/category_create.html', {'form': form})


@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_update.html', {'form': form})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category/category_delete.html', {'category': category})


# ==================================================================================

# Product CRUD views

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product/product_create.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/product_update.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product/product_delete.html', {'product': product})


# ==================================================================================


# Info CRUD views

@login_required
def info_list(request):
    infos = Info.objects.all()
    return render(request, 'info/info_list.html', {'infos': infos})

def info_detail(request, pk):
    info = get_object_or_404(Info, pk=pk)
    return render(request, 'info/info_detail.html', {'info': info})

@login_required
def info_create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.save()
            return redirect('info_detail', pk=info.pk)
    else:
        form = InfoForm()
    return render(request, 'info/info_create.html', {'form': form})

@login_required
def info_update(request, pk):
    info = get_object_or_404(Info, pk=pk)
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            info = form.save()
            return redirect('info_detail', pk=info.pk)
    else:
        form = InfoForm(instance=info)
    return render(request, 'info/info_update.html', {'form': form})

@login_required
def info_delete(request, pk):
    info = get_object_or_404(Info, pk=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('info_list')
    return render(request, 'info/info_delete.html', {'info': info})


# ==================================================================================


# Product Enter CRUD views

def product_enter_list(request):
    products = ProductEnter.objects.all()
    context = {'products': products}
    return render(request, 'product_enter/product_enter_list.html', context)


def product_enter_detail(request, pk):
    product_enter = get_object_or_404(ProductEnter, pk=pk)
    context = {'product_enter': product_enter}
    return render(request, 'product_enter/product_enter_detail.html', context)


def product_enter_create(request):
    product = Product.objects.all()
    context = {'products': product}


    if request.method == 'POST':
        ProductEnter.objects.create(
            product_id = request.POST['product_id'],
            quantity = request.POST['number'],
            date = request.POST['date'],
            description = request.POST['description'],
        )
        return redirect('product_enter_list')
    return render(request, 'product_enter/product_enter_create.html', context)

def product_enter_update(request, pk):
    product_enter = get_object_or_404(ProductEnter, pk=pk)
    if request.method == 'POST':
        form = ProductEnterForm(request.POST, instance=product_enter)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=pk)
    else:
        form = ProductEnterForm(instance=product_enter)
    context = {'form': form}
    return render(request, 'product_enter/product_enter_update.html', context)


def product_enter_delete(request, pk):
    product_enter = get_object_or_404(ProductEnter, pk=pk)
    if request.method == 'POST':
        product_enter.delete()
        return redirect('list_product_enter')
    context = {'product_enter': product_enter}
    return render(request, 'product_enter/product_enter_delete.html', context)

# ==================================================================================


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = WishList.objects.get_or_create(user=request.user, product=product)
    return redirect('product_detail', pk=product_id)

@login_required
def remove_from_wishlist(request, product_id):
    wishlist_item = get_object_or_404(WishList, user=request.user, product_id=product_id)
    wishlist_item.delete()
    return redirect('wishlist')

@login_required
def wishlist(request):
    wishlist_items = WishList.objects.filter(user=request.user)
    context = {'wishlist_items': wishlist_items}
    return render(request, 'wishlist.html', context)

# ==================================================================================


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(author=request.user, is_active=True)
    product_img = product.images.first()
    cart_product, created = CartProduct.objects.get_or_create(
        productImg=product_img,
        product=product,
        cart=cart
    )
    if not created:
        cart_product.quantity += 1
    cart_product.total_price = cart_product.quantity * product.price
    cart_product.save()
    return redirect('view_cart')


@login_required
def remove_from_cart(request, cart_product_id):
    cart_product = get_object_or_404(CartProduct, id=cart_product_id, cart__author=request.user)
    cart_product.delete()
    return redirect('view_cart')

@login_required
def view_cart(request):
    # Get all active carts for the user
    active_carts = Cart.objects.filter(author=request.user, is_active=True)
    
    # If multiple active carts exist, merge them into one
    if active_carts.count() > 1:
        main_cart = active_carts.first()
        for other_cart in active_carts[1:]:
            for cart_product in other_cart.cart_products.all():
                # Move products to the main cart
                cart_product.cart = main_cart
                cart_product.save()
            other_cart.delete()
    elif active_carts.count() == 0:
        # If no active cart exists, create a new one
        main_cart = Cart.objects.create(author=request.user, is_active=True)
    else:
        main_cart = active_carts.first()

    cart_products = main_cart.cart_products.all()
    total_price = sum(cp.total_price for cp in cart_products)
    context = {
        'cart': main_cart,
        'cart_products': cart_products,
        'total_price': total_price
    }
    return render(request, 'cart/view_cart.html', context)

@login_required
def update_cart_quantity(request, cart_product_id):
    cart_product = get_object_or_404(CartProduct, id=cart_product_id, cart__author=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_product.quantity = quantity
            cart_product.total_price = cart_product.quantity * cart_product.product.price
            cart_product.save()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, author=request.user, is_active=True)
    total_price = sum(cp.total_price for cp in cart.cart_products.all())
    
    if request.method == 'POST':
        cart.is_active = False
        cart.shopping_date = timezone.now()
        cart.save()
        return redirect('order_confirmation')
    
    return render(request, 'cart/checkout.html', {'cart': cart, 'total_price': total_price})

@login_required
def order_confirmation(request):
    latest_order = Cart.objects.filter(author=request.user, is_active=False).order_by('-shopping_date').first()
    return render(request, 'cart/order_confirmation.html', {'order': latest_order})