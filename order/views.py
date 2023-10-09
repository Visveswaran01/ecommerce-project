import json
import stripe
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import JsonResponse
from product.cart import Cart

from .models import Order, OrderItem,ShippingAddress

def process_order(request):

    cart = Cart(request)
    data = json.loads(request.body)
    total_price = 0

    items = []
    for item in cart:
        product = item['product']
        obj = {}

        obj['price_data'] = {

            'currency' : 'inr',

            'unit_amount' : product.price * 100,

            'product_data': {
                'name': product.name,
            },
           
        }

        obj['quantity'] = item['quantity']

        items.append(obj)
    
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='http://127.0.0.1:8000/success',
        cancel_url='http://127.0.0.1:8000/cart'
    )
    
    payment_intent = checkout_session.payment_intent

    address = data['address']
    zipcode = data['zipcode']
    city = data['city']
    state = data['state']
    phone = data['phone']

    place_address = ShippingAddress.objects.create(address=address,city=city,state=state,postal_code=zipcode,phone_number=phone)

    order = Order.objects.create(user=request.user,shipping_address=place_address)
    order.payment_intent = payment_intent
    order.paid_amount = cart.get_total_cost()
    order.paid = True
    order.save()


    for item in cart:
        product = item['product']
        quantity = int(item['quantity'])
        price = product.price * quantity

        item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
    
    cart.clear()

    return JsonResponse({'session': checkout_session, 'order': payment_intent})