from django.shortcuts import render
from.models import Category, Book

# Create your views here.
def book_list(request):
    books = Book.objects.select_related('category').all()
    return render(request, 'library/book_list.html', {'books': books})