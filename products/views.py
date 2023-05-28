from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import Item, OrderItem, Order


# Create your views here.
class ProductsView(ListView):
    model = Item
    paginate_by = 4
    template_name = 'products/products.html'

class ProductView(DetailView):
    model = Item
    template_name = 'products/product.html'

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            contex = {
                'object': order
            }
            return render(self.request, 'products/order_summary.html', contex)
        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have an active order ')
            return redirect("products:product")

def thank(request):
    return render(request, 'products/thank.html')

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity+=1
            order_item.save()
            messages.info(request, 'This item quantity was updated')
            return redirect('products:product', slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, 'This item was added to your cart')
            return redirect('products:product', slug=slug)
    else:
        orderDate = timezone.now()
        order = Order.objects.create(user=request.user, orderDate=orderDate)
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart')
        return redirect('products:product',slug=slug)

@login_required
def add_single_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity+=1
            order_item.save()
            messages.info(request, 'This item quantity was updated')
            return redirect('products:order_summary')
        else:
            order.items.add(order_item)
            messages.info(request, 'This item was added to your cart')
            return redirect('products:order_summary')
    else:
        orderDate = timezone.now()
        order = Order.objects.create(user=request.user, orderDate=orderDate)
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart')
        return redirect('products:order_summary')

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, 'This item was removed from your cart')
            return redirect('products:product', slug=slug)
        else:
            # add a message saying the user doesn't have an order
            messages.info(request, 'This item was not in your cart')
            return redirect('products:product', slug=slug)
    else:
        # add a message saying the user doesn't have an order
        messages.info(request, 'You do not have an active order ')
        return redirect('products:product', slug=slug)

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False)[0]
            order_item.quantity -= 1
            order_item.save()
            messages.info(request, 'This item quantity was updated')
            return redirect('products:order_summary')
        else:
            # add a message saying the user doesn't have an order
            messages.info(request, 'This item was not in your cart')
            return redirect('products:product', slug=slug)
    else:
        # add a message saying the user doesn't have an order
        messages.info(request, 'You do not have an active order ')
        return redirect('products:product', slug=slug)