from django.views import View
from store.models.product import Product
from django.shortcuts import render, HttpResponse
from store.models.order import Order


class OrderView(View):
    def get(self, request):
        userID = request.session['user_id']
        orders = Order.get_basket_by_customer(customer_id=userID)
        print(f'orders={orders}')
        context = {
            'orders': orders
        }
        # return HttpResponse('Твои заказы')
        return render(request, 'store/orders.html', context=context)
