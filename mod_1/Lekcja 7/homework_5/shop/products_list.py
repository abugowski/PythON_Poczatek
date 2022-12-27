
products = {
    "chleb":
        {
            "quantity": 10,
            "unit_price": 2.5,
        },
    "jabłka":
        {
            "quantity": 20,
            "unit_price": 1.5,
        }
}

def update_products_list(product, quantity):
    products[product]["quantity"] = products[product]["quantity"] - quantity
    return products
