from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Order

# Create your views here.

def index(request):
    product_objects = Product.objects.all()

    # search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name != None:
        product_objects = product_objects.filter(title__icontains=item_name)
    
    # pagination
    paginator = Paginator(product_objects, 2)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects':product_objects})


def detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object':product_object})

def checkout(request):

    if request.method == 'POST':
        item = request.POST.get('items', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        total = request.POST.get('total', '')
        order = Order(item=item, name=name, email=email, address=address, city=city, state=state, zip=zip, total=total)
        order.save()

    return render(request, 'shop/checkout.html')