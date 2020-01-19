from django.urls import path

from . import views

from .views import (
    delete_from_cart,
    cart_view,
    clean_cart,
  #  add_to_cart
)

urlpatterns = [
    path("", views.menu, name="menu"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path('cart', views.cart_view, name='cart'),
    path(r'item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
   # path(r'item/add/(?P<item_id>[-\w]+)/$', add_to_cart, name='add'),
    path(r'cart/clear', clean_cart, name='clean_cart'),
]
