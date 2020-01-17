from django.urls import path

from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path('cart', views.cart_view, name='cart')
]
