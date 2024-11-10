from django.shortcuts import render, HttpResponse
from django.db import connection
from .models import Product, Supplier
from django.db.models import Q

global_var = "Hello world!"
# Create your views here.
def index(request): #erti 
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM products")
    # print(cursor.fetchall())
    # prodact = Product.objects.create(name= 'asus vivobook', description = 'asus', price = '1500')

    # product =Product()
    # product.name = 'asus 700'
    # product.description = 'asus laptop'
    # product.price = 1400
    # product.save()


    # products = Product.objects.all()
    # print(products)

    # prodacts = Product.objects.filter(name__icontains= 'macbook').first()
    # print(prodacts)

    # products = Product.objects.filter(Q(name__icontains= 'asu') | Q(name__icontains= 'pro'))
    # print(products)

    # product = Product.objects.get(pk=4)
    # product.delete()


    # suppliers = Supplier.objects.all()
    # for supplier in suppliers:
    #     print(supplier.name)
    #     print(supplier.products.name)

    # suppliers = Supplier.objects.filter(products__name__icontains = 'asus').first()
    # print(suppliers)

    # supplier= Supplier.objects.select_related('products').all()
    # print(supplier)


    products = Product.objects.prefetch_related('category').all()
    print(products)
    for product in products:
        for category in product.category.all():
            print(f'{category.name} - {product.name}')
      
        
    return HttpResponse('<h1> Hello World!</h1>')

def test(request):
    return render(request, 'testhtml.html', {'variable': global_var})


def test2(request):
    return render(request, 'test2.html')