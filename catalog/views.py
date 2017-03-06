from django.shortcuts import render
from .models import Book, Author, BookInstance
# Create your views here.

def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_authors=Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_instances':num_instances, 'num_authors':num_authors}
    )
