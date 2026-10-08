
#===================ZADANIA SPRAWDZAJĄCE=========================#
# Pobierz odległość (kilometry) i czas (godzina) od użytkownika. Wylicz średnią prędkość
print(f'==============Kilometry=================')


# Pobierz przyprostokątne a i b. Oblicz przeciwprostokątną c. (Tw. Pitagorasa)
print(f"=============Pitagoras==================")

import math
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print(f'Przeciwprostokątna tego trójkątu wynosi: {math.sqrt(a*a + b*b)}')
#Parking ma 77 metrów długości. Jedno auto zajmuje 5 metrów, parkując równolegle. 
# Ile aut zmieści się na parkingu oraz ile miejsca pozostanie niewykorzystane?
print(f'===============Parking===================')
dlugosc_parkingu = 77
auto = 5

# Pobierz od użytkownika liczbę - x. Wylosuj liczbę z przedziału (x, x+10) i wyświetl.
print(f'=============Losowanie==================')



# Wprowadzenie do list (Gry losowe i zapisywanie wyników)
print(f'===============Totolotek=================')
min_liczba = 1
max_liczba = 60
import random

wylosowane_liczby = []

while len(wylosowane_liczby) < 6:
    liczba = 0 # Dopisz wzór na losowanie losowej liczby

    if liczba not in wylosowane_liczby:
        wylosowane_liczby.append(liczba)

wylosowane_liczby.sort()

print("Wylosowane liczby:")
print(wylosowane_liczby)


        


