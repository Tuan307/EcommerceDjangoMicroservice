import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Shoe

@csrf_exempt
def create_shoe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('Name')
        brand = data.get('Brand')
        color = data.get('Color')
        size = data.get('Size')
        price = data.get('Price')
        description = data.get('Description')
        for val in Shoe.objects.filter(name=name).all():
            return JsonResponse({'error': 'Shoe existed!'})
        
        if name and brand and color and size and price and description:
            shoe = Shoe(name=name, brand=brand, color=color, size=size, price=price, description=description)
            shoe.save()
            return JsonResponse({'message': 'Shoe created successfully!',
                                     'description' : {
                                        'ID' : shoe.id,
                                        'Name' : name,
                                        'Brand ' : brand,
                                        'Color' : color,
                                        'Size' : size,
                                        'Price' : price,
                                        'Description' : description
                                    }})
           
        else:
            return JsonResponse({'error': 'Please provide all fields!'})


@csrf_exempt
def delete_shoe(request, shoe_id):
    if request.method == 'DELETE':
        try:
            shoe = Shoe.objects.get(id=shoe_id)
            shoe.delete()
            return JsonResponse({'message': 'Shoe deleted successfully!',
                                 'description' : {
                                     'ID' : shoe_id
                                 }  
                                })
        except Shoe.DoesNotExist:
            return JsonResponse({'error': 'Invalid shoe id!'})

@csrf_exempt
def search_shoe(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        name = data.get('Shoe Name')
        if name:
            try:
                shoes = Shoe.objects.filter(name__icontains=name)
                data = []
                for shoe in shoes:
                    data.append({'ID': shoe.id, 'Name': shoe.name, 'Brand': shoe.brand.name, 'Color': shoe.color, 
                                'Size': shoe.size, 'Price': str(shoe.price), 'Description': shoe.description})
                return JsonResponse(data, safe=False)
            except Shoe.DoesNotExist:
                return JsonResponse({'error': 'Shoe not found!'})
    return JsonResponse({'error': 'Invalid request!'})
