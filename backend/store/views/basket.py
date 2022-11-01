from django.views import View
from store.models.product import Product
from django.shortcuts import render


class Basket(View):
    def get(self, request):
        IDs = list(request.session['basket'])
        products = Product.get_products_by_id(list_id=IDs)
        print(f'IDs= {IDs}')
        print(f'products= {products}')
        context = {
            'products': products
        }
        return render(request, 'store/basket.html', context=context)
