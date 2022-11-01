from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views import View
from store.models import Category, Product


class Home(View):
    def post(self, request):

        product = request.POST.get('product')
        remove = request.POST.get('remove')
        basket = request.session.get('basket')
        print(f'в классе Home basket= {basket}')
        if basket:
            count = basket.get(product)
            # print(f'count = {count}')
            if count:
                if remove:
                    if count <= 1:
                        basket.pop(product)
                    else:
                        basket[product] = count - 1
                else:
                    basket[product] = count + 1
            else:
                basket[product] = 1
        else:
            basket = {}
            basket.setdefault(product, 1)
            # basket[product]=1

        request.session['basket'] = basket
        request.session['testValue'] = 'Тут что-то есть'
        print(f'request.session.keys()={request.session.keys()}')
        print(f'request.session.get("testValue") = {request.session.get("testValue")}')
        if request.session.get("category"):
            return redirect(f'store/?category={request.session.get("category")}')
        else:
            return redirect('home')

    def get(self, request):
        # print(f'class Home в def get()')
        # print(f' request.get_full_path = {request.get_full_path()}| {request.get_full_path()[1:]}')
        # print(f'request.GET.get("category")={request.GET.get("category")}')
        # print(f'get_port = {request.get_port}')
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
        # return HttpResponse('Домашняя страница')


def store(request):
    basket = request.session.get('basket')
    category = request.session.get('category')
    if not basket:
        request.session['basket'] = {}
        request.session['category'] = 0
    category_id = request.GET.get('category')
    request.session['category'] = category_id
    context = {
        'categories': Category.get_all_categories,
        'products': Product.get_all_products_by_category_id(category_id),
    }
    return render(request, 'store/home.html', context=context)


def product_profile(request, product_id):
    context = {
        'products': Product.get_all_products(),
        'product_id': product_id,
        'product': Product.get_products_by_id(product_id).get(),
        # 'skip': True
    }
    return render(request, 'store/product_profile.html', context=context)
    # return HttpResponse(f'Индекс товара - {product_id} test= {test}')
