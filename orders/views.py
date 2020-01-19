from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import PizzaType, Topping, Sub, SicilianPizzaType, Pasta, Salad, DinnerPlatter, Product, Order
from django.db.utils import OperationalError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.
try:
    def menu(request):
        sub = Product.objects.filter(name='Sub')
        context = {
            "menu": PizzaType.objects.all(),
            "toppings": Topping.objects.all(),
            "PizzaType": PizzaType.objects.all(),
            "subs": Sub.objects.all(),
            "sicilian": SicilianPizzaType.objects.all(),
            "pasta": Pasta.objects.all(),
            "salad": Salad.objects.all(),
            "platter": DinnerPlatter.objects.all(),
            "user": request.user,
            "users": render(request, 'users/login.html'),
            "sub": sub,
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



def add_to_cart(request, **kwargs):
    # get the user id
  #  user = get_object_or_404(Customer, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # create order item of selected product
    order_item, status = Order.objects.get_or_create(items=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=request.user.id, fulfilled=status)
    user_order.items.add(order_item)
    messages.info(request, "item added to cart")



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
    item_to_delete = Order.objects.filter(owner=request.user.id, fulfilled=False, pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect(reverse('cart'))


@login_required()
def clean_cart(request):
    delete = Order.objects.filter(owner=request.user.id, fulfilled=False)
    if delete.exists():
        for item in delete:
            item.delete()
    return redirect(reverse('cart'))
