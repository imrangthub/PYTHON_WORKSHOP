from django.shortcuts import render, redirect
from .services import BookService
from .forms import BookForm

def index(request):
    return render(request, 'index.html')

# List all books
def book_list(request):
    books = BookService.get_all_books()
    return render(request, 'book_list.html', {'books': books})

# Create a new book
def book_create(request):
    if request.method == "POST":
        if BookService.create_book(request.POST):
            return redirect('book_list')
    return render(request, 'book_form.html', {'form': BookForm(), 'action': 'Create'})

# Edit a book
def book_update(request, id):
    book = BookService.get_book_by_id(id)
    if request.method == "POST":
        if BookService.update_book(id, request.POST):
            return redirect('book_list')
    return render(request, 'book_form.html', {'form': BookForm(instance=book), 'action': 'Update'})

# Delete a book
def book_delete(request, id):
    if request.method == "POST":
        BookService.delete_book(id)
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': BookService.get_book_by_id(id)})
