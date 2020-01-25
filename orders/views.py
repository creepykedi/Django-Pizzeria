from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topping, Product, Order, CompletedOrder
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
                username = form.cleaned_data.get('username')
                messages.success(request, f"Account created for {username}!")
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
                messages.success(request, f"Welcome, {user}. Thanks for logging in.")
                return redirect('menu')
        else:
            form = AuthenticationForm()

        return render(request, 'users/login.html', {'form': form})


    def logout_view(request):
        logout(request)
        return redirect("login")

    def success_view(request):
        return redirect("orders/success.html")

except OperationalError:
    pass


def cart_view(request):
    order = Order.objects.filter(owner=request.user.id, fulfilled=False)
    owner = request.user.username
    total_price = []
    order_numb = []
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
            total_price.extend(product.price for product in user_order_items)
            # access whole order from where we can get topping info and order id
            order_numb.append(order)
    # calculating cart total
    total_price = sum(total_price)

    context = {
        "owner": owner,
        "total_price": total_price,
        "item_id": item_id,
        "toppings": Topping.objects.all(),
        "order_numb": order_numb,
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
    messages.success(request, f"{product} added to cart.")
    return redirect(reverse('menu'))


@login_required()
def clean_cart(request):
    delete = Order.objects.filter(owner=request.user.id, fulfilled=False)
    if delete.exists():
        for item in delete:
            item.delete()
    return redirect(reverse('cart'))


def fulfill_order(request):
    items_to_order = Order.objects.filter(owner=request.user.id, fulfilled=False)
    if items_to_order.exists():
        for order in items_to_order:
            order.fulfilled = True
            order.save()
            CompletedOrder(order=order).save()
    return render(request, "orders/success.html")


def select_topping(request, topping, order_id):
    topping = Topping.objects.filter(topping=topping)
    anorder = Order.objects.filter(pk=order_id).first()
    for topping in topping:
        anorder.toppingchoice = topping.topping
        anorder.save()
    return redirect(reverse('cart'))


def add_topping(request, order_id, item_type):
    if request.method == "POST":
        top = request.POST['topselect']
        order = Order.objects.filter(pk=order_id).first()
        print(item_type)
        topping_list = []
        print(top)
        order.toppingchoice = top
        order.save()
        """ 
        if '2' in item_type:
            print('ye')
            topping_list.clear()
            if len(topping_list) < 2:
                topping_list.append(top)
                print(topping_list)
            else:
                order.toppingchoice = topping_list
                order.save()
                topping_list.clear()
        """
    return redirect(reverse('cart'))
