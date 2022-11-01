from django import template

register = template.Library()


@register.filter(name='is_in_basket')
def is_in_basket(product, basket):
    keys = basket.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='basket_amount')
def basket_amount(product, basket):
    keys = basket.keys()
    print(f'keys= {keys}')
    for id in keys:
        if int(id) == product.id:
            # print(f'basket.filter(id) ={basket.filter(pk=id)}')
            # print(f'basket.get(id) = {basket.get(id)}')
            return basket.get(id)
    return 0


@register.filter(name='price')
def price(product, basket):
    print(f'в def price(product, basket):')
    print(f'product = {product} basket = {basket}')

    return product.price * basket_amount(product, basket)


@register.filter(name='total_basket_price')
def total_basket_price(products, basket):
    print(f'в def total_basket_price')
    print(f'products= {products} basket= {basket}')
    sum = 0

    for item in products:
        print(f'item= {item}')
        sum += price(item,basket)

    return sum