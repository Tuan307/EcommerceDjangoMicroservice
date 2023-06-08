from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
import json, random


def __create_book(title, author, category, published_date, price, description):
    id = random.randint(1, 100)
    new_book = Book(id = id, title=title, author=author, category=category, published_date=published_date, price=price, description=description)
    new_book.save()
    return new_book.id

@csrf_exempt
def create_book(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            title = val1.get("Title")
            author = val1.get("Author")
            category = val1.get("Category")
            published_date = val1.get("Published Date")
            price = val1.get("Price")
            description = val1.get("Description")
            

            if title and author and category and published_date and price and description:
                respdata = __create_book(title, author, category, published_date, price, description)
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Added book.'
                resp['data'] = {'Book ID': respdata}
            else:     
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def remove_book(request, book_id):
    resp = {}
    if request.method == 'DELETE':
        try:
            product = Book.objects.all().get(id=str(book_id))
            product.delete()
            resp['message'] = 'Product deleted successfully'
            return HttpResponse(json.dumps(resp), content_type='application/json')
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Product not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
       

@csrf_exempt
def book_search(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            search_term = val1.get("search_term")
            if search_term:
                books = Book.objects.all().filter(Q(id__icontains=search_term) |Q(title__icontains=search_term))
                books_list = []
                for book in books:
                    book_dict = {}
                    book_dict['id'] = book.id
                    book_dict['title'] = book.title
                    book_dict['author'] = book.author
                    book_dict['category'] = book.category
                    book_dict['published_date'] = book.published_date.strftime('%Y-%m-%d')
                    book_dict['price'] = str(book.price)
                    book_dict['description'] = book.description
                    books_list.append(book_dict)
                    
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Books retrieved successfully'
                resp['data'] = books_list
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Search term is required.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Invalid content type.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Invalid request method.'
        
    return HttpResponse(json.dumps(resp), content_type = 'application/json')


@csrf_exempt
def get_books(request):
    resp = {}
    if request.method == 'GET':
        books = Book.objects.all()
        books_list = []
        for book in books:
            book_dict = {}
            book_dict['id'] = book.id
            book_dict['title'] = book.title
            book_dict['author'] = book.author
            book_dict['category'] = book.category
            book_dict['published_date'] = book.published_date.strftime('%Y-%m-%d')
            book_dict['price'] = str(book.price)
            book_dict['description'] = book.description
            books_list.append(book_dict)
                    
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Books retrieved successfully'
            resp['data'] = books_list
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Invalid request method.'
        
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

