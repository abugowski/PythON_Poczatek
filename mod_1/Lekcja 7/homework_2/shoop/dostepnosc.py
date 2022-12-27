
products = [
    {
        "name": "chleb",
        'quantity': 5,
        'unit_price': 6
    },
    {
        "name": "jabłka",
        'quantity': 14,
        'unit_price': 12,
    }
]

def select_product(product):
    for produkt in products:
        if produkt['name'] == product:
            return produkt

def product_exist(product):
    if not select_product(product):
        return False
    return True
