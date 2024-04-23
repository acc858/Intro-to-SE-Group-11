from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import random 
from .models import Seller, listing, Buyer
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from decimal import Decimal

from .forms import SellerReg, SellerLogForm, BuyerLogForm, BuyerReg, BuyerUpdate, SellerUpdate

# Create your views here.
def index(request):
    return render(request, "home/login.html")

def AddListing(request):
    return render(request, "home/AddListing.html")

def AccountSeller(request):
    seller = Seller.objects.get(user=request.user)
    return render(request, 'home/AccountSeller.html', {'seller': seller})

def logout(request):
    return render(request, "home/logout.html")

def login(request):
    return render(request, "home/login.html")

def Create_Account(request):
    return render(request, "home/Create_Account.html")

def Create_AccountBuy(request):
    return render(request, "home/Create_AccountBuy.html")

def loginbuy(request):
    return render(request, "home/loginbuy.html")

def AccountUser(request):
    return render(request, "home/AccountUser.html")

def UpdateUser(request):
    return render(request, "home/UpdateUser.html")

def UpdateSeller(request):
    return render(request, "home/UpdateSeller.html")

def Buyer_Home(request):
    listings = listing.objects.all()
    return render(request, "home/Buyer_Home.html",  {'listings': listings})

def Seller_Home(request):
    seller = Seller.objects.get(user=request.user)
    seller_listings = listing.objects.filter(seller=seller)
    return render(request, "home/Seller_Home.html",  {'listings': seller_listings})


#Cart Functions

def add_to_cart(request, book_id):
    book = get_object_or_404(listing, pk=book_id)
    cart = request.session.get('cart', {})
    
    # Check if the book is already in the cart
    if str(book_id) in cart:
        # Check if the quantity in the cart is less than the available quantity
        if cart[str(book_id)] < book.quantity:
            # Increase the quantity in the cart by 1
            cart[str(book_id)] += 1
    else:
        # If the book is not in the cart, add it with a quantity of 1
        cart[str(book_id)] = 1
    
    request.session['cart'] = cart
    return redirect('Buyer_Home')



def User_Cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for book_id, quantity in cart.items():
        book = get_object_or_404(listing, pk=book_id)
        # Calculate the quantity added to the cart instead of using the book's quantity
        added_quantity = min(quantity, book.quantity)
        cart_items.append({'book': book, 'quantity': added_quantity})
        total_price += book.price * added_quantity
    return render(request, 'home/User_Cart.html', {'cart_items': cart_items, 'total_price': total_price})


def delete_from_cart(request, book_id):
    if 'cart' in request.session:
        cart = request.session['cart']
        if str(book_id) in cart:
            # Check if the quantity is greater than 1
            if cart[str(book_id)] > 1:
                # If yes, decrease the quantity by 1
                cart[str(book_id)] -= 1
            else:
                # If not, delete the book from the cart
                del cart[str(book_id)]
            request.session['cart'] = cart
    return redirect('User_Cart')
#end of cart functions


#Seller Create account and login
def reg_seller(request):
    if request.method == 'POST':
        form = SellerReg(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            balance = 0
            
            user = User.objects.create_user(email=email, username=username, password=password)
            new_seller = Seller(user=user, email=email, username=username, balance=balance)
            new_seller.save()
            return redirect('login')


    else:
        form = SellerReg()
    return render(request, 'home/Create_Account.html', {'form': form})


def sellerlogin(request):
    if request.method == 'POST':
        form = SellerLogForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    seller = Seller.objects.get(user=user)
                    auth_login(request, user)
                    return redirect('AccountSeller')
                except Seller.DoesNotExist:
                    messages.error(request, 'Invalid username or password')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    
    else:
        form = SellerLogForm()
    return render(request, 'home/login.html', {'form': form})


#BUYER Create account and login
def reg_buyer(request):
    if request.method == 'POST':
        form = BuyerReg(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(email=email, username=username, password=password)
            new_buyer = Buyer(user=user, email=email, username=username)
            new_buyer.save()
            return redirect('loginbuy')


    else:
        form = BuyerReg()
    return render(request, 'home/Create_AccountBuy.html', {'form': form})


def buyerlogin(request):
    if request.method == 'POST':
        form = BuyerLogForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    buyer = Buyer.objects.get(user=user)
                    auth_login(request, user)
                    return redirect('AccountUser')
                except Buyer.DoesNotExist:
                    messages.error(request, 'Invalid username or password')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    
    else:
        form = BuyerLogForm()
    return render(request, 'home/loginbuy.html', {'form': form})

    

@login_required
def createlisting(request):
    if request.method == 'POST':
        # Retrieve listing details from the form
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        quantity = request.POST.get('quantity')
        isbn = request.POST.get('isbn')
        price = request.POST.get('price')
        seller = Seller.objects.get(user=request.user)
        #images
        image=request.POST.get('image')
        # Create a new Listing object
        new_listing = listing(
            title=title,
            author=author,
            year=year,
            quantity=quantity,
            isbn=isbn,
            price=price,
            seller=seller,
            image=image
            
            
        )
        new_listing.save()

        # Redirect to a success page or another page
        return redirect('AccountSeller')  # Assuming 'home' is the name of the home page URL pattern

    return render(request, 'home/AddListing.html')  # Render the listing creation form

@login_required
def delete_listing(request, listing_id):
    # Retrieve the listing
    listing_to_delete = get_object_or_404(listing, pk=listing_id)

    # Check if the listing belongs to the logged-in seller
    if listing_to_delete.seller.user == request.user:
        listing_to_delete.delete()
        messages.success(request, 'Listing deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this listing.')

    return redirect('Seller_Home')

@login_required
def update_buy(request):
    if request.method == 'POST':
        form = BuyerUpdate(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            user = request.user  # Assuming the user is logged in
            user.username = new_username
            user.save()
                # Redirect to a success page
            return redirect('AccountUser')
    else:
        form = BuyerUpdate()
    return render(request, 'home/AccountUser.html', {'form': form})

@login_required
def update_sell(request):
    if request.method == 'POST':
        form = SellerUpdate(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            user = request.user  # Assuming the user is logged in
            user.username = new_username
            user.save()
                # Redirect to a success page
            return redirect('AccountSeller')
    else:
        form = SellerUpdate()
    return render(request, 'home/AccountSeller.html', {'form': form})

# all of the checkout functions
def checkout_pay(request):
   
    if request.method == 'POST':
        #This is all of the payment information
        card_hold_name = request.POST.get('card_hold_name')
        card_num = request.POST.get('card_num')
        exp = request.POST.get('exp')
        cvv = request.POST.get('cvv')

        #This is all of the shipping Information
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address_main = request.POST.get('address_main')
        address_opt = request.POST.get('address_opt')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        #return render(request, 'home/checkout_review.html',
        return render(request, 'home/checkout_review.html',{
            'card_hold_name': card_hold_name,
            'card_num': card_num,
            'exp': exp,
            'cvv': cvv,

            'full_name': full_name,
            'email': email,
            'address_main': address_main,
            'address_opt': address_opt,
            'city': city,
            'state': state,
            'zip': zip,
        })
    else:
        return render(request, 'home/checkout_pay.html')

def checkout_review(request):
    if request.method == 'POST':
        # Retrieve payment information from the form
        card_hold_name = request.POST.get('card_hold_name', '')
        card_num = request.POST.get('card_num', '')
        exp = request.POST.get('exp', '')
        cvv = request.POST.get('cvv', '')
        
        # Assuming you also have shipping information collected in checkout_pay.html
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')
        address_main = request.POST.get('address_main', '')
        address_opt = request.POST.get('address_opt', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')

        # You can do further processing or validation here

        # Retrieve cart items from the session
        if 'cart' in request.session:
            cart_items = []
            total_price = 0
            for book_id, quantity in request.session['cart'].items():
                book = get_object_or_404(listing, pk=book_id)
                cart_items.append({'book': book, 'quantity': quantity})
                total_price += book.price * quantity
            print("Cart Items:", cart_items)  # Add this line for debugging

            # Pass cart items, payment, and shipping information to the template
            return render(request, 'home/checkout_review.html', {
                'cart_items': cart_items,
                'total_price': total_price,
                'card_hold_name': card_hold_name,
                'card_num': card_num,
                'exp': exp,
                'cvv': cvv,
                'full_name': full_name,
                'email': email,
                'address_main': address_main,
                'address_opt': address_opt,
                'city': city,
                'state': state,
                'zip_code': zip_code,
            })
        else:
            return render(request, 'home/checkout_review.html', {
                'cart_items': [],
                'total_price': 0,
                'card_hold_name': card_hold_name,
                'card_num': card_num,
                'exp': exp,
                'cvv': cvv,
                'full_name': full_name,
                'email': email,
                'address_main': address_main,
                'address_opt': address_opt,
                'city': city,
                'state': state,
                'zip_code': zip_code,
            })
    else:
        # Handle GET request, redirect user to appropriate page or show error
        return HttpResponse("Method Not Allowed", status=405)
    
def confirm_checkout(request):
    total_cost = Decimal(0)

#Update the inventory and seller's balance
    for item_id, quantity in request.session.get('cart', {}).items():
        # Retrieve the listing corresponding to the item_id
        inventory_item = get_object_or_404(listing, pk=item_id)

#Calculate the total cost
        total_cost += inventory_item.price * quantity

        # Update the seller's balance
        seller = inventory_item.seller
        seller.balance += inventory_item.price * quantity
        seller.save()

        # Subtract the quantity from the inventory
        inventory_item.quantity -= quantity
        if inventory_item.quantity <= 0:
            inventory_item.delete()
        else:
            inventory_item.save()

    # Clear the cart after checkout
    request.session['cart'] = {}

    # Redirect to the home page
    return redirect('Buyer_Home')
    
  
