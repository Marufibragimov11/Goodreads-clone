from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from books.models import Book


# # Generic View
# class BooksView(ListView):
#     template_name = "books/list.html"
#     queryset = Book.objects.all()
#     context_object_name = "books"
#     paginate_by = 2


# Simple View
class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        page_size = request.GET.get('page_size', 2)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        return render(request, "books/list.html", {"page_obj": page_obj})


class BookDetailedView(DetailView):
    template_name = "books/detail.html"
    pk_url_kwarg = "id"
    model = Book

# class BookDetailedView(View):
#     def get(self, request, id):
#         book = Book.objects.get(id=id)
#         return render(request, "books/detail.html", {"book": book})
