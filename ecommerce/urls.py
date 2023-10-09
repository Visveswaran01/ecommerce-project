"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views

from core.views import homePage,signUpView,signIn,signoutView
from product.views import view_store,add_to_cart,viewCart,checkout,update_cart,hx_menu_cart,hx_cart_total,remove_from_cart,hx_checkout_btn,success,hx_cart_product,view_product
from order.views import process_order

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('core.urls')),

    path('shop', view_store, name='shop'),
    path('product/<int:pid>',view_product,name="viewproduct"),

    path('cart',viewCart,name="cart"),
    path('add_to_cart/<int:pid>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pid>',remove_from_cart,name='remove_from_cart'),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),


    path('hx_menu_cart',hx_menu_cart,name="hx_menu_cart"),
    path('hx_cart_total',hx_cart_total,name="hx_cart_total"),
    path('hx_checkout_btn',hx_checkout_btn,name="hx_checkout_btn"),
    path('hx_cart_product',hx_cart_product,name="hx_cart_product"),


    path('checkout',checkout,name='checkout'),
    path('success',success,name='success'),
    path('process_order', process_order, name='process_order'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
