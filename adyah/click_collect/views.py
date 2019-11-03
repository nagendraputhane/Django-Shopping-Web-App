from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Locality, Shop, Item, CartItems
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    context = {
        "shops": Shop.objects.all()
    }
    return render(request, "click_collect/index.html", context)

def shop(request, shop_id):

    try:
        shop = Shop.objects.get(pk=shop_id)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist.")
    context = {
        "shop": shop,
        "items": shop.items.all(),
        "no_items": Item.objects.exclude(shops=shop).all(),
    }
    return render(request, "click_collect/shops.html", context)

def logout_view(request):
    logout(request)
    return render(request, "authentication/login.html", {"message": "Logged out."})

def book(request):
    cart_item = request.POST["content"]
    new_item = CartItems(content = cart_item)
    new_item.save()
    context = {
        "items": CartItems.objects.all()
    }
    return render(request, "click_collect/items.html", context)
