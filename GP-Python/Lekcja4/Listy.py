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

#Zadanie dodatkowe (Oblicz cenę całkowitą)



# Pobierz od użytkownika liczbę produktu i wypisz nazwę tego produktu

# Funkcja len mówi nam jak długa jest nasza lista
dlugosc = len(lista_zakupow)
print(f"Ilość elementów: {dlugosc}")
