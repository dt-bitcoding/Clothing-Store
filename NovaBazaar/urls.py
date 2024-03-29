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

    # password reset urls for the user
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
    path("changepassword/", views.change_password, name="changepassword"),
    # product related urls for the user
    path("add_product/", views.add_product, name="add_product"),

    path("product_detail/<int:id>", views.product_detail, name="product_detail"),
    
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add-to-cart'),
    path('cart-list', views.cart_list, name='cart-list'),
    
    path("remove-from-cart/<int:id>/", views.remove_from_cart, name="remove-from-cart"),


    path("cart/", views.cart_detail, name="cart"),
    path("address/", views.address, name="address"),

    path("buy-now/<int:product_id>", views.buy_now, name="buy-now"),

    path("category/", views.category_page, name="category"),
    path("profile/", views.profile, name="profile"),
    path("orders/", views.orders, name="orders"),
    path("search/", views.search_view, name="search"),
    path("registration/", views.customer_registration, name="customerregistration"),
    path("checkout/<int:product_id>", views.checkout, name="checkout"),
    path("uploadimg/", views.upload_form, name="uploadimg"),

    # payment urls
    path("payment/", views.payment, name="payment"),
    path("paypal-return/", views.paypal_return, name="paypal-return"),
    path("paypal-cancel/", views.paypal_cancel, name="paypal-cancel"),
]
