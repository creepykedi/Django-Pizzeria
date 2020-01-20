from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topping, Product, Order
from django.db.utils import OperationalError
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.contrib import messages
# Create your views here.
try:
    def menu(request):
        context = {
            "menu": Product.objects.all(),
            "toppings": Topping.objects.all(),
            "regular": Product.objects.filter(name='Regular Pizza'),
            "sicilian": Product.objects.filter(name='Sicilian Pizza'),
            "pasta": Product.objects.filter(name='Pasta'),
            "salad": Product.objects.filter(name='Salads'),
            "platter": Product.objects.filter(name='Dinner Platters'),
            "user": request.user,
            "users": render(request, 'users/login.html'),
            "sub": Product.objects.filter(name='Sub'),
            "product": Product.objects.all()
        }
        return render(request, "orders/menu.html", context)

    def signup_view(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                # log the user in
                return redirect('menu')
        else:
            form = UserCreationForm()
        return render(request, 'users/signup.html', {'form': form})

    def login_view(request):
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('menu')
        else:
            form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})


    def logout_view(request):
        logout(request)
        return redirect("login")



except OperationalError:
    pass



def cart_view(request):
    order = Order.objects.filter(owner=request.user.id, fulfilled=False)
    owner = request.user.username
    orders_list = []
    total_price = []
    item_id = []
    # if order exists
    if order:
        for order in order:
            # adding id in this Order
            item_id.extend([order.id])
            user_order = order
            # access order items
            user_order_items = user_order.items.all()
            # add them to the list
            orders_list.extend(product for product in user_order_items)
            total_price.extend(product.price for product in user_order_items)
    # calculating cart total
    total_price = sum(total_price)

    context = {
        "owner": owner,
        "order": order,
        "orders_list": orders_list,
        "total_price": total_price,
        "item_id": item_id
    }
    return render(request, "orders/cart.html", context)


@login_required()
def delete_from_cart(request, item_id):
    # getting product instance by its id
    product = Product.objects.filter(pk=item_id).first()
    # getting query set of this item from this user
    item_to_delete = Order.objects.filter(owner=request.user.id, fulfilled=False, items=product.id)
    if item_to_delete.exists():
        item_to_delete.delete()
    return redirect(reverse('cart'))


@login_required()
def add_to_cart(request, item_id):
    # get the user
    buyer = User.objects.filter(id=request.user.id).first()
    # get the instance of a product by its id
    product = Product.objects.get(pk=item_id)
    # create order for the user and save
    newOrder = Order(owner=buyer)
    newOrder.save()
    # associate this order with the product
    newOrder.items.add(product)
    return redirect(reverse('menu'))


@login_required()
def clean_cart(request):
    delete = Order.objects.filter(owner=request.user.id, fulfilled=False)
    if delete.exists():
        for item in delete:
            item.delete()
    return redirect(reverse('cart'))
