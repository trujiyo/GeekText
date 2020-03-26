from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Profile, Order, OrderItem
#C.S. imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import F
from datetime import date
import random
import string
import datetime

# Create your views here.

#S.T. views for home page and book details pages
@login_required #C.S. added this
def index(request):
    Books = Book.objects.all()
    #C.S. edits to index
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]

    context = {
        'Book': Books,
        'current_order_products': current_order_products
    }
    return render(request, "BookDetails/index.html", context)

def bookDetails(request, title):
    book = get_object_or_404(Book, book_name=title)
    return render(request, 'BookDetails/bookDetails.html', {'Book': book}) 

#C.S. views for Shopping Cart feature
def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str

def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Book.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    #return redirect(reverse('product_list')) S.T. changed this back to index
    return redirect(reverse('index'))

@login_required()
def add_quantity_from_cart(request,item_id):
    item_to_add = OrderItem.objects.filter(pk=item_id).update(quantity=F('quantity') + 1)
    messages.info(request, "This books quantity added.")
    return redirect(reverse('order_summary'))

@login_required()
def reduce_quantity_from_cart(request,item_id):
    item_to_reduce = OrderItem.objects.filter(pk=item_id)
    if item_to_reduce[0].quantity < 2:
        item_to_reduce[0].delete()
        messages.info(request, "Book has been removed since quantity less than 1")
    else:
        item_to_reduce.update(quantity=F('quantity') - 1)
        messages.info(request, "This books quantity reduced.")
    return redirect(reverse('order_summary'))

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Book has been removed")
    return redirect(reverse('order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'BookDetails/order_summary.html', context)


@login_required()
def checkout(request):
    OrderItem.objects.all().delete()
    messages.info(request, "Thank you, order processed.")
    return redirect(reverse('order_summary'))