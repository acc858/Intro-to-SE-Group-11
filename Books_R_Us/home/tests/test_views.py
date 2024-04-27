from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.models import Buyer, Seller, listing, Purchase, Notification, Admin, Return_Notification
import json

# VIEWS TESTS
class TestViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.index_url = reverse('index')
    
    def test_project_list_GET(self):
        c = Client()
        response = c.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index')

#Buyer test
class BuyerTestCase(TestCase):
    def setUp(self):
        #Buyer creation test 1
        self.buyer = Buyer.objects.create(email="testbuyer@gmail.com", username= "testbuyer", password="testbuyer")

    def test_buyer_creation(self):
        buyer= Buyer.objects.get(email="testbuyer@gmail.com")
        self.assertEqual(buyer.username, "testbuyer")
    
    #Checks for incorrect username


#Seller test
class SellerTestCase(TestCase):
    def setUp(self):
        self.seller = Seller.objects.create(email="testseller@gmail.com", username= "testseller", password="testseller")

    def test_seller_creation(self):
        seller= Seller.objects.get(email="testseller@gmail.com")
        self.assertEqual(seller.username, "testseller")

#Listings test
class ListingTestCase(TestCase):
    def setUp(self):
        self.Listing = listing.objects.create(
            title="test",
            author="test",
            year=0000,
            quantity= 0,
            isbn= 9788888888888,
            price= 0,
            seller="testseller",
            image="www.test.com")

    def test_listing_creation(self):
        Listing= listing.objects.get(title="test")
        self.assertEqual(Listing.title, "test")
        self.assertEqual(Listing.author, "test")
        self.assertEqual(Listing.year, 0000)
        self.assertEqual(Listing.quantity, 0)
        self.assertEqual(Listing.isbn, 9788888888888)
        self.assertEqual(Listing.price, 0)
        self.assertEqual(Listing.seller, "testseller")
        self.assertEqual(Listing.image, "www.test.com")

    def test_listing(self):
        self.assertEqual(str(self.Listing), "test")
        self.assertEqual(str(self.Listing.author), "test")


        