Punkty = 5
print(f"Punkty: {Punkty}")
Punkty = "Trzynaście"
print(f"Punkty: {Punkty}")

zycia_calkowite = 12
zycia_pozostale = 4
zycia_zuzyte = zycia_calkowite - zycia_pozostale
print(f"Zużyto {zycia_zuzyte} żyć ")

# wartość int - liczba całkowita
liczba = 41
print(f"{liczba} - typ:{type(liczba)}")
# wartość string - ciąg znaków
zdanie = "Nie lubię C++"
print(f"{zdanie} - typ:{type(zdanie)}")

# Czemu typy są ważne
punkty = int(input("Daj liczbe"))
print(f"Punkty z handicappem: {punkty + 3}")

#Zczytywanie liczb całkowitych (typ int)
liczba1 = int(input("Daj liczbę: "))
liczba2 = int(input("Daj liczbę: "))
print(f"Liczba 1: {liczba1} Liczba 2: {liczba2}")

licz1 = 14
licz2 = 8
print(f"Dodawanie: {licz1 + licz2}") 
print(f"Odejmowanie: {licz1 - licz2}")
print(f"Mnożenie: {licz1 * licz2}")
print(f"Dzielenie: {licz1 / licz2}")

# Try - spróbuj coś zrobić
# except - jeśli się nie uda
x = input("Podaj x: ")
try:
    x = int(x)
    print("Konwersja udana")
except:
    print("Nie udało się")