from django.urls import path
from . import views




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
    path('return_purchase/<int:purchase_id>/', views.return_purchase, name='return_purchase'),
    path('Create_AccountBuy/', views.Create_AccountBuy,name='Create_AccountBuy'),
    path('loginbuy/', views.loginbuy, name='loginbuy'),
    path('buyerlogin/', views.buyerlogin, name="buyerlogin"),

    path('AccountUser/', views.AccountUser, name='AccountUser'),
    path('AccountSeller/', views.AccountSeller, name='AccountSeller'),
    path('UpdateUser/', views.UpdateUser, name='UpdateUser'),
    path('UpdateSeller/', views.UpdateSeller, name='UpdateSeller'),
    path('update_buy/', views.update_buy, name='update_buy'),
    path('update_sell/', views.update_sell, name='update_sell'),

    path('dismiss_notification/<int:notification_id>/', views.dismiss_notification, name='dismiss_notification'),
    path('dismiss_return_notification/<int:return_notification_id>/', views.dismiss_return_notification, name='dismiss_return_notification'),

    path('Buyer_Home/', views.Buyer_Home, name='Buyer_Home'),
    path('Seller_Home/', views.Seller_Home, name='Seller_Home'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('User_Cart/', views.User_Cart, name='User_Cart'),
    path('delete_from_cart/<int:book_id>/', views.delete_from_cart, name='delete_from_cart'),

    path('add_to_comp/<int:book_id>/', views.add_to_comp, name='add_to_comp'),
    path('book_comp/', views.book_comp, name='book_comp'),
    path('delete_from_comp/<int:book_id>/', views.delete_from_comp, name='delete_from_comp'),

    path('checkout_pay/',views.checkout_pay,name='checkout_pay' ),
    path('checkout_review/',views.checkout_review,name='checkout_review'),
    path('confirm_checkout/', views.confirm_checkout, name='confirm_checkout'),

    path('search/', views.search, name='search'),

    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('delete_buyer/<int:buyer_id>/', views.delete_buyer, name='delete_buyer'),
    path('delete_seller/<int:seller_id>/', views.delete_seller, name='delete_seller'), 
    path('delete_listing/<int:listing_id>/', views.delete_listing, name='delete_listing'),
    path('loginadmin', views.loginadmin, name='loginadmin'),
    path('Admin_Home/', views.Admin_Home, name='Admin_Home'),
    
]