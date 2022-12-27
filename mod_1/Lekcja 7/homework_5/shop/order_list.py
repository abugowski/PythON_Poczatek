
from shop.products_list import products, update_products_list

orders = [
    {}
]

def create_new_order(product, quantity):

    unit_price = products[product]['unit_price']
    product_availabilty = products[product]['quantity']

    if product_availabilty < quantity:
        print("Nie masz tylu artykułów")
        return None

    total_price = unit_price * quantity


    new_order = {
        'product': product,
        'quantity': quantity,
        'total_price': total_price
    }

    orders.append(new_order)
    update_products_list(product, quantity)

    return new_order



