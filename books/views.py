from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from books.models import Book


# # Generic View
class BooksView(ListView):
    template_name = "books/list.html"
    queryset = Book.objects.all()
    context_object_name = "books"


# # Simple View
# class BooksView(View):
#     def get(self, request):
#         books = Book.objects.all()
#         return render(request, "books/list.html", {"books": books})


class BookDetailedView(DetailView):
    template_name = "books/detail.html"
    pk_url_kwarg = "id"
    model = Book

# class BookDetailedView(View):
#     def get(self, request, id):
#         book = Book.objects.get(id=id)
#         return render(request, "books/detail.html", {"book": book})
