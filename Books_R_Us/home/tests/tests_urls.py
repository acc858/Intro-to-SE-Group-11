from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, logout, login, AccountSeller
import json

# URLS TESTS

class TestUrls(SimpleTestCase):
    def test_url_index(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_url_login(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_url_logout(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout) 

    def test_url_AccountSeller(self):
        url = reverse('AccountSeller')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AccountSeller)

    def test_call_login(self):
        response = self.client.get('/url/to/view', follow=True)
        self.assertRedirects(response, '/login/')
        response = self.client.post('/url/to/view', follow=True)
        self.assertRedirects(response, '/login/')

    def test_call_logout(self):
        response = self.client.get('/url/to/view', follow=True)
        self.assertRedirects(response, '/logout/')
        response = self.client.post('/url/to/view', follow=True)
        self.assertRedirects(response, '/logout/')