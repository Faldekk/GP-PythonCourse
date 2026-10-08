print(f'=================Lista zakupów================')
# Lista zawiera teksty (stringi)
lista_zakupow = ["chleb", "ser", "mleko", "czekolada"]

print(lista_zakupow[0])  # Wynik: chleb (To jest pierwszy element!)
print(lista_zakupow[3])  # Wynik: czekolada (To jest ostatni element)
print(lista_zakupow) #tak można wyświetlić całą zawartość listy

lista_zakupow[1] = "żółty ser" # Zmieniamy element o indeksie 1 ("ser")

lista_zakupow.append("biały ser") # funckja append dodaje do listy

lista_zakupow.remove("czekolada") # funkcja remove usuwa z listy

lista_zakupow[2] = "kefir"
lista_zakupow.append("rzodkiewki")
lista_zakupow.append("masło")
lista_zakupow.append("daktyle")
lista_zakupow.remove("rzodkiewki")

ceny = [5.50, 9.0, 2.99, 4.49, 10, 11]
print(ceny)
print(f"Cena chleba: {ceny[0]}")

print("---Zakupy---")
print(f"{lista_zakupow[0]}: {ceny[0]} zł")
print(f"{lista_zakupow[1]}: {ceny[1]} zł")
print(f"{lista_zakupow[2]}: {ceny[2]} zł")
print(f"{lista_zakupow[3]}: {ceny[3]} zł")
print(f"{lista_zakupow[4]}: {ceny[4]} zł")
print(f"{lista_zakupow[5]}: {ceny[5]} zł")

#Zadanie dodatkowe (Oblicz cenę całkowitą)\
cena_calkowita = 0
for i in lista_zakupow:
    cena_calkowita+=i
print(cena_calkowita)

dlugosc = len(lista_zakupow)
print(f"Ilość elementów: {dlugosc}")

plecak = ["zeszyt", "laptop", "kanapka", "piórnik"]

print(f"Pierwsza rzecz (indeks 0): {plecak[0]}")
print(f"Ostatnia rzecz (indeks 3): {plecak[3]}")
print(plecak)

import random
numer = random.randint(0, len(plecak))
print(f"Losowy przedmiot: {plecak[numer]}")

nowy = input("Podaj nowy przedmiot: ")

print(f'Zawartość plecaka: {plecak}')

numer = int(input("Podaj numer elementu do zmiany: "))
nowy = input("Podaj nową wartość dla tego elementu: ")

print(f'Zawartość plecaka: {plecak}')

do_usuniecia = input("Który element usunąć: ")

print(f'Zawartość plecaka: {plecak}')

print(f'W plecaku jest {len(plecak)} przedmiotów')


