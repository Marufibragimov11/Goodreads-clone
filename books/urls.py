from django.urls import path

from .views import BooksView, BookDetailedView


app_name = "books"
urlpatterns = [
    path("", BooksView.as_view(), name="list"),
    path("<int:id>/", BookDetailedView.as_view(), name="detail"),
]