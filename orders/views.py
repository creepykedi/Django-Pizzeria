from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import PizzaType, Topping, Category, Sub, SicilianPizzaType, Pasta, Salad, DinnerPlatter
from django.db.utils import OperationalError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


        """ 
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
     
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"), {'form': form})
        else:
            return render(request, "users/login.html", {"message": "Invalid credentials"})
        """


    def logout_view(request):
        logout(request)
        return redirect("login")


except OperationalError:
    pass

