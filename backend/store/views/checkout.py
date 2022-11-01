from django.views import View
from django.shortcuts import redirect
from store.models.product import Product
from store.models.order import Order
from store.models.infoUser import InfoUser


class СheckOut(View):
    def post(self, request):
        address = request.POST['address_']
        phone = request.POST.get('phone_')
        user_id = request.session['user_id']
        basket = request.session['basket']
        print(basket)
        products = Product.get_products_by_id(list_id=list(basket.keys()))
        for product in products:
            order = Order(
                customer=InfoUser(id=user_id),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                amount=basket[f'{product.id}']
            )
            order.save()
        request.session['basket'] = {}
        return redirect('basket')
