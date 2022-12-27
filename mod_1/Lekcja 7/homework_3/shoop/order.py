
from shoop.dostepnosc import product_exist
from shoop.dostepnosc import select_product

def order():
    product = input("Podaj nazwę produktu, X żeby zkończyć: ")
    order_list = []
    while product != 'X':
        if product_exist(product):
            quantity = int(input("Podaj ilość: "))
            kupujemy = select_product(product)
            order_list.append({'name': product, "quantity": quantity, 'price': kupujemy['unit_price'] * quantity})
            product = input('Podaj następny produckt lub X żeby zakończyć: ')
        else:
            product = input("Nie ma takiego produktu, podaj inny lub X żeby zkończyć: ")
    return order_list