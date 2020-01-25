from django.urls import path

from . import views

from .views import (
    delete_from_cart,
    cart_view,
    clean_cart,
    add_to_cart,
    fulfill_order,
    select_topping,
    add_topping
)

urlpatterns = [
    path("", views.menu, name="menu"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path('cart', views.cart_view, name='cart'),
    path(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    path(r'^cart/clear', clean_cart, name='clean_cart'),
    path(r'^item/add/(?P<item_id>[-\w]+)/$', add_to_cart, name='add'),
    path(r'^cart/$', fulfill_order, name='fulfill'),
    path(r'^cart/(?P<topping>-<order_id>[-\w]+)/<int:order>/$', select_topping, name='select_topping'),
    path(r'^add_topping/<int:order_id>(?P^/d<item_type>[^/]+)/$', add_topping, name='add_topping'),
    path("success", views.success_view, name="success"),
]
