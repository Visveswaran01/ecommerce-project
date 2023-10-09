from django.conf import settings
from product.models import Product
from decimal import Decimal



class Cart(object):

    #   Initializing the cart / retriving the previous cart if existed
    def __init__(self,request):
        self.session = request.session
        cart  = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart

    """
    
        |Level 1                |   Level2  
        |-----------------------|---------------------------------------------
        |   key : product id    |   Key1 : quantity      created/modified by : add_item                
        |                       |   key2 : item          created/modified by : __iter__ , get_total_cost
        |                       |   key3 : total_price   created/modified by : __iter__

    """

    def __iter__(self):

        #retrive the product while iterating
        for pid in self.cart.keys():
            self.cart[pid]['product'] = Product.objects.get(pk=int(pid))
        
        #calculating the price and return generator
        for item in self.cart.values():
            item["total_price"] = Decimal(item["product"].price) * item["quantity"]
            yield item
    

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_products_purchased(self):
        return len(self.cart.keys())
    
    
    def get_total_cost(self):
        for pid in self.cart.keys():
            self.cart[pid]['product'] = Product.objects.get(pk=int(pid))

        return int(sum(Decimal(item["product"].price) * item['quantity'] for item in self.cart.values()))

    #   save the current state of cart after performing cart functionalities
    def save(self): 
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    #   cart Functionalities : add , remove
    def add_items(self, product_id, quantity=1, update_quantity=False):

        product_id = str(product_id)

        #create the item if it doesnot exist in cart
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'pid' : int(product_id)}
        
        #update the quantity of item in the cart

        if update_quantity:
            self.cart[product_id]['quantity'] += quantity

            if self.cart[product_id]['quantity'] == 0:
                self.remove_items(product_id)

        else:
            self.cart[product_id]['quantity'] = quantity
        
        #Once operations are performed save the modifications made in the cart
        self.save()


    
    def remove_items(self,product_id):

        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    def get_item(self, product_id):

        product_id = str(product_id)

        if product_id in self.cart:
            up_item = self.cart[product_id]
            return up_item
        else:
            return None


