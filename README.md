# REST
rest_api which fetches data from external source

instructions to run:
1. git clone https://github.com/godfatherofdevil/REST.git
2. python -m venv env
3. pip install -r requirements.txt
4. cd to project directory
5. python manage.py runserver
6. the endpoints will be at -
 a) http://localhost:8000/api/v1/books/
 b) http://localhost:8000/api/v1/authors
 
 to get the list of books sorted by published date pass query param "published" like below:
 http://localhost:8000/api/v1/books?published=DESC  --> pass ASC to get in ascending order
 
 to get the list of books sorted by title pass query param "title" like below:
 http://localhost:8000/api/v1/books?title=DESC --> pass ASC to get in ascending order
