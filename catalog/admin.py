from django.contrib import admin
from .models import Author, Book, BookInstance

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)