from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
import json


from django.views.decorators.csrf import csrf_exempt


def store(request):
    category = request.GET.get('category')
    if category == None:
        products = Product.objects.order_by('-price').filter(is_published=True)
        page_num = request.GET.get("page")
        paginator = Paginator(products, 3)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        products = Product.objects.filter(category__name=category)
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'store/store.html', context)


def productDetail(request, pk):
    eachProduct = Product.objects.get(id=pk)
    context = {'eachProduct': eachProduct}
    return render(request, 'store/product_detail.html', context)


def cart(request):

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(name__icontains=query)
            return render(request, 'store/searchbar.html', {'products': products})
        else:
            print("No information to show")
            return render(request, 'store/searchbar.html', {})


def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        user=user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if(orderItem.quantity <= 0):
        orderItem.delete()
    return JsonResponse('It was added', safe=False)
