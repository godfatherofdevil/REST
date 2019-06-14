from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json

@api_view(['GET'])
def books_view(request):

    if request.method == "GET":
        books_url = "https://hokodo-frontend-interview.netlify.com/data.json"
        try:
            data = requests.get(books_url)
        except Exception:
            return HttpResponse(status=404)
        json_data = data.json()
        books = json_data["books"]

        # support for sorting by published date 
        # query params should be passed like this -> ?published=ASC or ?published=DESC
        # for title, -> ?title=ASC or ?title=DESC
        published_order = request.query_params.get("published", None)
        title_order = request.query_params.get("title", None)
        if published_order is not None:
            books = sorted(books, key=lambda k:k['published'], reverse=(published_order=="DESC"))
            return JsonResponse(books, status=data.status_code, safe=False)
        if title_order is not None:
            books = sorted(books, key=lambda k:k['title'], reverse=(title_order=="DESC"))
            return JsonResponse(books, status=data.status_code, safe=False)

        return JsonResponse(json_data, status=data.status_code)

@api_view(['GET'])
def author_view(request):

    if request.method == "GET":
        books_url = "https://hokodo-frontend-interview.netlify.com/data.json"
        try:
            data = requests.get(books_url)
        except Exception:
            return HttpResponse(status=404)
        json_data = data.json()
        books = json_data["books"]

        author_books = {}
        for book in books:
            if book['author'] not in author_books:
                author_books[book['author']] = [book]
            else:
                author_books[book['author']].append(book)
        
        return JsonResponse(author_books, status=data.status_code)

