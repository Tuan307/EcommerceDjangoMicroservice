import random, json, requests
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_book(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)
            category_name = data.get('Category Name')
            author_name = data.get('Author Name')
            book_title = data.get('Book Title')
            published_date = data.get('Publishded Date')
            price = data.get('Price')
            description = data.get('Description')

            if category_name and author_name and book_title and published_date and price and description:
                book_id = requests.post('http://127.0.0.1:2100/books/books/create/', json={
                    "Author" : author_name,
                    "Category" : category_name,
                    "Title" : book_title,
                    "Published Date" : published_date,
                    "Price" : price,
                    "Description" : description
                }).json()
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Successfully registered.'
                resp['data'] = {
                    "Title" : book_title,
                    "Author" : author_name,
                    "Category" : category_name,
                    "Published Date" : published_date,
                    "Price" : price,
                    "Description" : description,
                    "Book" : book_id
                } 
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type='application/json')



@csrf_exempt
def delete_book(request,book_id):
    if request.method == 'DELETE':
        delete_response = requests.delete('http://127.0.0.1:2100/books/books/delete/'+str(book_id)+'/').json()
        return HttpResponse(str(json.dumps(delete_response)))
    return HttpResponse("ERROR")

@csrf_exempt
def get_books(request):
    url = "http://127.0.0.1:2100/books/books/get_all_books/"
    list_book = requests.get(url).json()
    return HttpResponse(json.dumps(list_book), content_type='application/json')


@csrf_exempt
def book_search(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)
            p_name = data.get('search_term')
            print(p_name)
            if p_name :
                book_list = requests.post('http://127.0.0.1:2100/books/books/search/', json={
                    "search_term" : p_name,
                }).json()
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['data'] = {
                    "Books" : book_list,
                } 
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')



@csrf_exempt
def register_shoes(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)
            p_name = data.get('Name')
            b_name = data.get('Brand')
            color = data.get('Color')
            size = data.get('Size')
            price = data.get('Price')
            description = data.get('Description')

            if p_name and b_name and color and size and price and description:
                requests.post('http://127.0.0.1:2200/shoes/create_shoe/', json={
                    "Name" : p_name,
                    "Brand" : b_name,
                    "Color" : color,
                    "Size" : size,
                    "Price" : price,
                    "Description" : description
                }).json()
                shoes_id = requests.get('http://127.0.0.1:2200/shoes/search_shoe/', json={
                    "Shoe Name" : p_name,
                }).json()
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Successfully registered.'
                resp['data'] = {
                    "Name" : p_name,
                    "Brand" : b_name,
                    "Color" : color,
                    "Size" : size,
                    "Price" : price,
                    "Description" : description, 
                    "Shoes" : shoes_id, 
                } 
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def register_clothes(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần thêm
            # Name, Brand ID,  Category, Size, Price, Description
            p_name = data.get('Product Name')
            b_name = data.get('Brand Name')
            category = data.get('Category')
            size = data.get('Size')
            price = data.get('Price')
            description = data.get('Description')
            if p_name and b_name and category and size and price and description:
                requests.post('http://127.0.0.1:2300/clothes/create_brand/', json={
                    "Brand Name" : b_name
                }).json()
                brand_id = requests.get('http://127.0.0.1:2300/clothes/search_brand/', json={
                    "Brand Name" : b_name
                }).json()
                print(brand_id)
                shoes_id = requests.post('http://127.0.0.1:2300/clothes/create_clothing/', json={
                    "Name" : p_name,
                    "Brand ID" : brand_id['ID'],
                    "Category" : category,
                    "Size" : size,
                    "Price" : price,
                    "Description" : description
                }).json()
                print(shoes_id)
                shoes_id = requests.get('http://127.0.0.1:2300/clothes/search_clothing/', json={
                    "Clothing Name" : p_name,
                }).json()
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Successfully registered.'
                resp['data'] = {
                    "Brand" : brand_id, 
                    "Shoes" : shoes_id, 
                } 
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type='application/json')