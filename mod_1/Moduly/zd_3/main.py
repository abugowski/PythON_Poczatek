
import calculations.calculations

kapital = float(input("Podawj wartość kapitału początkowego: "))
oprocentowanie = float(input("Podaj oprocentowanie lokaty: "))
okres = float(input("Podaj okres lokaty: "))

wartosc = calculations.calculations.calculations(kapital, oprocentowanie, okres)
print(f"Wartość lokaty po {int(okres)} latach wyniesie {wartosc:.2f}")
