from django.urls import path
from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.index, name="index") ,

    path('reg_seller/', views.reg_seller, name='reg_seller'),
    path('reg_buyer/', views.reg_buyer, name='reg_buyer'),

    path('AddListing/', views.AddListing, name="AddListing"),
    path('AccountSeller/', views.AccountSeller, name="AccountSeller"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('Create_Account/', views.Create_Account, name="Create_Account"),
    
    path('sellerlogin/', views.sellerlogin, name='sellerlogin'),
    path('createlisting/', views.createlisting, name="createlisting"),
    path('delete_listing/<int:listing_id>/', views.delete_listing, name='delete_listing'),
    path('Create_AccountBuy/', views.Create_AccountBuy,name='Create_AccountBuy'),
    path('loginbuy/', views.loginbuy, name='loginbuy'),
    path('buyerlogin/', views.buyerlogin, name="buyerlogin"),

    path('AccountUser/', views.AccountUser, name='AccountUser'),
    path('AccountSeller/', views.AccountSeller, name='AccountSeller'),
    path('UpdateUser/', views.UpdateUser, name='UpdateUser'),
    path('UpdateSeller/', views.UpdateSeller, name='UpdateSeller'),
    path('update_buy/', views.update_buy, name='update_buy'),
    path('update_sell/', views.update_sell, name='update_sell'),


    path('Buyer_Home/', views.Buyer_Home, name='Buyer_Home'),
    path('Seller_Home/', views.Seller_Home, name='Seller_Home'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('User_Cart/', views.User_Cart, name='User_Cart'),
    path('delete_from_cart/<int:book_id>/', views.delete_from_cart, name='delete_from_cart'),

    path('checkout_pay/',views.checkout_pay,name='checkout_pay' ),
    path('checkout_review/',views.checkout_review,name='checkout_review'),
    path('confirm_checkout/', views.confirm_checkout, name='confirm_checkout'),

    path('search/', views.search, name='search'),
    path('books/', include('booksearch.urls')),

]