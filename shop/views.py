from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    product_objects = Products.objects.all()

    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

   #paginator code
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('Items', "")
        name = request.POST.get('Name', "")
        email = request.POST.get('Email', "")
        address = request.POST.get('Address', "")
        city = request.POST.get('City', "")
        state = request.POST.get('State', "")
        zipcode = request.POST.get('Zipcode', "")
        total = request.POST.get('Total', "")
        order_list = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order_list.save()

    return render(request, 'shop/checkout.html')
