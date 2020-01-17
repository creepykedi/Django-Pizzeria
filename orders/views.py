from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import PizzaType, Topping, Category, Sub, SicilianPizzaType, Pasta, Salad, DinnerPlatter, Customer, Product, Order
from django.db.utils import OperationalError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.
try:

    def menu(request):
       # if not request.user.is_authenticated:
       #    return render(request, "users/login.html", {"message": None})
        context = {
            "menu": PizzaType.objects.all(),
            "toppings": Topping.objects.all(),
            "category": Category.objects.all(),
            "PizzaType": PizzaType.objects.all(),
            "subs": Sub.objects.all(),
            "sicilian": SicilianPizzaType.objects.all(),
            "pasta": Pasta.objects.all(),
            "salad": Salad.objects.all(),
            "platter": DinnerPlatter.objects.all(),
            "user": request.user,
            "users": render(request, 'users/login.html')
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


    def cart_view(request):
        pass

except OperationalError:
    pass


def add_to_cart(request, **kwargs):
    # get the user id
    user = get_object_or_404(Customer, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # create order item of selected product
    order_item, status = Order.objects.get_or_create(items=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user, fulfilled=status)
    user_order.items.add(order_item)
    messages.info(request, "item added to cart")
