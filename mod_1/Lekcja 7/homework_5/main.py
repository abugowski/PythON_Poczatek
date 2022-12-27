from shop.order_list import create_new_order

print("Witaj w moim sklepie")
product = input("Co chciałbyś zamówić? ")
quantity = int(input("Ile chcesz zamówić? "))

total_price = create_new_order(product, quantity)['total_price']
print(f"Całkowity koszt zakupów {total_price} PLN.")
