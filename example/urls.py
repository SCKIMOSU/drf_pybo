from django.urls import path, include
from .views import HelloAPI, booksAPI, bookAPI, BooksAPI, BookAPI


urlpatterns = [
    path('hello/', HelloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/books/<int:bid>/", bookAPI),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/books/<int:bid>", BookAPI.as_view()),
]