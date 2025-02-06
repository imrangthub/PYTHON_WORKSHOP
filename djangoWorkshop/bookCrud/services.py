from django.shortcuts import get_object_or_404
from .models import Book
from .forms import BookForm

class BookService:
    @staticmethod
    def get_all_books():
        return Book.objects.all()

    @staticmethod
    def get_book_by_id(id):
        return get_object_or_404(Book, id=id)

    @staticmethod
    def create_book(data):
        form = BookForm(data)
        if form.is_valid():
            return form.save()
        return None

    @staticmethod
    def update_book(id, data):
        book = get_object_or_404(Book, id=id)
        form = BookForm(data, instance=book)
        if form.is_valid():
            return form.save()
        return None

    @staticmethod
    def delete_book(id):
        book = get_object_or_404(Book, id=id)
        book.delete()
