from books.views import books_view, author_view
from django.urls import path

urlpatterns = [
    path('books/', books_view),
    path('authors/', author_view),
]
