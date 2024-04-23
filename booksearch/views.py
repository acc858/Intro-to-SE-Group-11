from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.db.models import Q
from .forms import SearchForm

from django.http import HttpResponse
from home.models import listing 
def index(request):
    return HttpResponse("Welcome to the Booksearch app!")
def book_list(request):
    books = listing.objects.all()
    book_titles = "<br>".join([book.title for book in books])
    return HttpResponse(f"List of Books:<br>{book_titles}")
def search(request):
    form = SearchForm(request.GET)
    listings = None
    if form.is_valid():
        query = form.cleaned_data['query']
        try:
            isbn_query = int(query)  # Convert query to int to search ISBN
            listings = listing.objects.filter(Q(title__icontains=query) | Q(isbn=isbn_query))
        except ValueError:
            listings = listing.objects.filter(title__icontains=query)  # Fallback to title search if query is not an integer
    return render(request, 'search.html', {'form': form, 'listings': listings})



