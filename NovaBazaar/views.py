import uuid
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import User
from .forms import Form, MyForm, ProductForm, CustomerForm
from NovaBazaar.models import User, Product, Category
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from NovaBazaar.forms import ProductForm
from flask import Flask
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Cart
from django.core.exceptions import ValidationError
from django.contrib import messages


User = get_user_model()


def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    return render(
        request, "NovaBazaar/home.html", {"products": products, "category": category}
    )


def contact(request):
    return render(request, "NovaBazaar/contact.html")


def about(request):
    return render(request, "NovaBazaar/about.html")


def signup(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            print(request.POST)
            firstname = request.POST.get("FirstName")
            print("Firstname ", firstname)
            email = request.POST.get("Email", "")
            password = request.POST.get("Password", "")
            confirmPassword = request.POST.get("Confirm_password", "")

            user_instance = User(
                FirstName=firstname,
                Email=email,
                Password=password,
                confirm_password=confirmPassword,
            )
            user_instance.save()
            form.save()

            return redirect("login")
    else:
        form = MyForm()

    return render(request, "NovaBazaar/index.html", {"form": form})


def Userlogin(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        Password = request.POST.get("Password", "")
        user = authenticate(request, email=email, password=Password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "User Invalid. Try Again !")
            return redirect("login")
    else:
        form = Form()
    return render(request, "NovaBazaar/login.html", {"form": form})


def success_view(request):
    return render(request, "NovaBazaar/home.html")


def pass_reset_form(request):
    if request.method == "POST":
        with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS,
        ) as connection:
            recipient_list = request.POST.get("email").split()
            bcc_list = ["dt.bitcoding@gmail.com", "demo.darshil@yopmail.com"]

            # Create an EmailMessage instance
            email = EmailMessage(
                subject="Sending to the Testing Email",
                body="http://127.0.0.1:9898/password_reset_complete/",
                from_email="demo.darshil@yopmail.com",
                to=recipient_list,
                bcc=bcc_list,  # Make sure bcc is a list or tuple
                connection=connection,
            )

            # Now you can send the email
            email.send()

        return redirect("/password_reset_done")

    else:
        form = PasswordResetForm()
    return render(request, "NovaBazaar/pass_reset_form.html", {"form": form})


def pass_reset_confirm(request):
    return render(request, "NovaBazaar/pass_reset_confirm.html")


def pass_reset_done(request):
    return render(request, "NovaBazaar/pass_reset_done.html")


def pass_reset_complete(request):
    return render(request, "NovaBazaar/pass_reset_complete.html")


def logout(request):
    return render(request, "NovaBazaar/index.html")


def product_detail(request, id, *args, **kwargs):
    product = get_object_or_404(Product, id=id)
    return render(request, "NovaBazaar/productdetail.html", {"product": product})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("home")
    else:
        form = ProductForm()

    return render(request, "NovaBazaar/add_product.html", {"form": form})

def cart_list(request):
    carts = Cart.objects.filter(user=request.user)
    return render(request, "NovaBazaar/cart.html", {'carts': carts})

@login_required
def add_to_cart(request, id):
    # print("sdfsdf", request.method)
    carts = Cart.objects.filter(user=request.user)
    # print("cart", carts)
    if carts.filter(product=id).exists():
        # print("id", id)
        cart = Cart.objects.get(product=id, user=request.user)
        cart.count += 1
        cart.save()
        
    else:
        product = Product.objects.get(id=id)
        # print("product", product)
        Cart.objects.create(product=product, user=request.user, count=1)
    return redirect("cart-list")

@login_required
def remove_from_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")
    return redirect('cart-list')

@login_required
def cart_detail(request):
    return render(request, "NovaBazaar/cartdetail.html")

def buy_now(request):
    return render(request, "NovaBazaar/buynow.html")


def category_page(request):
    print(request.GET.get("id"))
    products = Product.objects.filter(category__id=request.GET.get("id"))
    category = Category.objects.all()

    return render(
        request, "NovaBazaar/mobile.html", {"products": products, "category": category}
    )


@login_required
# def profile(request):
#     if request.method == "POST":
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             name = request.POST.get("name")
#             address = request.POST.get("address")
#             city = request.POST.get("city")
#             state = request.POST.get("state")
#             zipcode = request.POST.get("zipcode")
#             form = Customer(
#                 name=name, address=address, city=city, state=state, zipcode=zipcode
#             )
#             form.save()
#             return redirect("home")
#     else:
#         form = CustomerForm()
#     return render(request, "NovaBazaar/profile.html", {"form": form})


def profile(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id = request.user.id
            profile.save()

    else:
        form = CustomerForm()

    return render(request, "NovaBazaar/profile.html", {"form": form})


def orders(request):
    return render(request, "NovaBazaar/orders.html")


def change_password(request):
    return render(request, "NovaBazaar/changepassword.html")


def customer_registration(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            email = request.POST.get("Email", "")
            password = request.POST.get("Password", "")
            confirmPassword = request.POST.get("Confirm_password", "")

            if password != confirmPassword:
                return HttpResponse("Password and Confirm Password not matched")
            else:
                form.save()
                return redirect("login")
    else:
        form = MyForm()
    return render(request, "NovaBazaar/customer_registration.html", {"form": form})


def checkout(request):
    return render(request, "NovaBazaar/checkout.html")


def address(request):
    return render(request, "NovaBazaar/address.html")


def search_view(request):
    query = request.GET.get("q")
    results = User.objects.filter(FirstName__icontains=query)
    context = {"query": query, "results": results}
    return render(request, "NovaBazaar/search.html", context)


def upload_form(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        context = {"form": ProductForm()}
        return render(request, "NovaBazaar/mobile.html", context)

    context = {"form": ProductForm()}
    return render(request, "NovaBazaar/mobile.html", context)


def payment(request):
    host = request.get_host()
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": str(uuid.uuid4()),
        "currency_code": "USD",
        "notify_url": request.build_absolute_uri(reverse("paypal-ipn")),
        "return_url": request.build_absolute_uri(reverse("payment_done")),
        "cancel_return": request.build_absolute_uri(reverse("payment_cancelled")),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "NovaBazaar/payment.html", context)


def paypal_return(request):
    messages.success(request, "Payment was successful")
    return redirect("home")


def paypal_cancel(request):
    messages.error(request, "Payment was cancelled")
    return redirect("home")
