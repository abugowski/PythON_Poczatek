
import math

def calculate_c(a, b):
    return math.sqrt(pow(a, 2) + pow(b, 2))

a = float(input("Podaj długość przyprostokątnej a: "))
b = float(input("Podaj długość przyprostokątnej b: "))

c = calculate_c(a, b)

print(f"Długość przeciwprostokątnej c wynosi {c}")
