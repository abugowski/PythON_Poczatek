
import avg_speed

dystans = float(input("Podaj dystans "))
czas = float(input("Podaj czas "))
speed = avg_speed.avg_speed(dystans, czas)
print(f"Średnia prędkość wynosi {speed}km/h")