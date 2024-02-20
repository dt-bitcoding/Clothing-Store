from django.urls import path
from . import views
from .views import success_view, add_to_cart, remove_from_cart, cart_detail

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("signup/success/", success_view, name="success"),
    path("loginuser", views.Userlogin, name="login"),
    path("logout/", views.logout, name="logout"),
    path("reset_password/", views.pass_reset_form, name="reset_password"),
    path(
        "password_reset_confirm/", views.pass_reset_confirm, name="pass_reset_confirm"
    ),
    path("password_reset_done/", views.pass_reset_done, name="password_reset_done"),
    path(
        "password_reset_complete/",
        views.pass_reset_complete,
        name="password_reset_complete",
    ),
    path("product_detail/", views.product_detail, name="product_detail"),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path("remove/<int:id>/", views.remove_from_cart, name="remove-from-cart"),
    path("cart/", views.cart_detail, name="cart"),
    path("address/", views.address, name="address"),
    path("buy/", views.buy_now, name="buy-now"),
    path("mobile/", views.mobile, name="mobile"),
    path("profile/", views.profile, name="profile"),
    path("orders/", views.orders, name="orders"),
    path("search/", views.search_view, name="search"),
    path("changepassword/", views.change_password, name="changepassword"),
    path("registration/", views.customerregistration, name="customerregistration"),
    path("checkout/", views.checkout, name="checkout"),
]
