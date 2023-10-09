from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .cart import Cart
from django.conf import settings

# Create your views here.

"""
    view of SHOP 
"""

def view_store(request):

    if request.user.is_authenticated:
        products = Product.objects.all()
        categories = Category.objects.all()
        active_category = str(request.GET.get('category',''))

        if active_category:
            products = Product.objects.filter(category__slug = active_category)

        context = {
                'products' : products,
                'categories' : categories,
                'active_cat' : active_category,
                }
        
        return render(request, 'product/shop.html', context)
    else:
        messages.error(request,"Please Login to view the shop")
        return redirect("/")

def view_product(request,pid):
    
    prod = Product.objects.get(id = pid)

    if request.POST:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        reviews = Review.objects.filter(user=request.user, product=prod)

        if reviews.count() > 0:
            review = reviews.first()
            review.rating = rating
            review.comment = comment
            review.save()
        else:
            review = Review.objects.create(
                product=prod,
                rating=rating,
                comment=comment,
                user=request.user
            )
            
    return render(request, 'product/individual_product.html', {'item' : prod})
    


"""
    CRUD Functionalities of Cart
"""

def add_to_cart(request,pid):

    cart = Cart(request)
    cart.add_items(pid)

    return render(request,'product/partials/basket.html')


def viewCart(request):
    cart = Cart(request)
    return render(request, 'product/cartsummary.html')


def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add_items(product_id, 1, True)
    else:
        cart.add_items(product_id, -1, True)
    
    c = cart.get_item(product_id)
   
    item = {}
    item['pid'] = product_id

    
    if c is not None:
        item['quantity'] = cart.get_item(product_id)['quantity']
        pd = Product.objects.get(pk = int(product_id))
        item['product'] = {
                                'id' : pd.id,
                                'price' : pd.price,
                                'name' : pd.name,
                                'img' : pd.img
        }

        item["total_price"] = item["quantity"] * pd.price
    else:
        item['quantity'] = 0

   
    response = render(request, 'product/partials/display_bkItems.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


def remove_from_cart(request,pid):

    cart = Cart(request)
    cart.remove_items(pid)

    return render(request,'product/partials/basket.html')
    

"""
    Helper Functions to update the potion of view in Cart at required situations
"""
def hx_menu_cart(request):
    return render(request,'product/partials/basket.html')

def hx_cart_total(request):
    return render(request,'product/partials/bk_cost.html')

def hx_checkout_btn(request):
    return render(request,'product/partials/checkout_button.html')

def hx_cart_product(request):
    return render(request,'product/partials/bk_display_ctlr.html')


"""
    Checkout page and defining the success page after checkout
"""

@login_required(login_url='/')
def checkout(request):
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE 
    return render(request,'product/checkout.html',{'pub_key' : pub_key})


def success(request):
    messages.success(request,"Your order has been placed Successfully.\nThanks for making the purchase")
    return redirect('home')



