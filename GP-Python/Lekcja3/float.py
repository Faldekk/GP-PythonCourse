# Przypomnienie poprzedniej lekcji

print("=============Powtórka==============")
imie = "Jan"
nazwisko = "Kowalski"
wiek = 18  # zczytywanie wieku użytkownika jako liczba całkowita
wzrost = 1.77

print(f'{imie} {nazwisko}, {wiek} lat, {wzrost}m wzrostu')

print(f'{imie}: {type(imie)}')
print(f'{nazwisko}: {type(nazwisko)}')
print(f'{wiek}: {type(wiek)}')
print(f'{wzrost}: {type(wzrost)}')

# TODO : zczytaj i wypisz od użytkownika jego wzrost i przypisz go do zmiennej wzrost. 
# Pamiętaj, że wzrost jest liczbą zmiennoprzecinkową (float).
print("=============Wczytywanie wzrostu==============")


# TODO : użyj try catch aby obsłużyć sytuację, gdy użytkownik poda niepoprawną 
# wartość wzrostu (np. tekst zamiast liczby). 
# W przypadku błędu wypisz komunikat o błędzie i przypisz zmiennej wzrost wartość 0.0. 
# Jeśli użytkownik poda poprawną wartość, przypisz ją do zmiennej wzrost i wypisz komunikat 
# o poprawnym wczytaniu wzrostu i wypisz typ i wartość zmiennej wzrost.

print("=============Obsługa błędów==============")



# TODO: napisz równanie, którego wynikiem jest liczba zmiennoprzecinkowa (float) i wypisz wynik oraz typ zmiennej

# TODO: policz średnią ocen
print("=============Średnia ocen==============")




# TODO: użyj operatora floor division (//) aby policzyć ile pełnych paczek kabla można zrobić z podanej długości kabla. Wypisz wynik oraz typ zmiennej.
print("=============Podział kabla na paczki==============")




# konwersja typów zmiennych. Co się dzieje, gdy konwertujemy float na int? Sprawdźmy to.
print("=============Konwersja typów zmiennych==============")

x = int(6.7)
print(f'{x}: {type(x)}')


# TODO: użyj operatora modulo (%) aby policzyć ile kabli zostanie po zrobieniu pełnych paczek. Wypisz wynik oraz typ zmiennej.
print("=============Reszta kabla==============")


# Potęgowanie w Pythonie odbywa się za pomocą operatora **. 
# TODO: Zczytaj od użytkownika liczbę i potęgę, a następnie wypisz wynik potęgowania oraz typ zmiennej.
print("=============Potęgowanie==============")
liczba = int(input("Podaj liczbe: "))
potega = int(input("Podaj potege: "))
print(f'{liczba} do potegi {potega} = {liczba ** potega}')
# Rounding liczb zmiennoprzecinkowych w Pythonie odbywa się za pomocą funkcji round(). Co to znaczy rounding?
print("=============funckje wbudowane==============")

print(f" (6.7): {round(6.7)}")

print(f" {abs(-10)}")

print(f": {len('Hello world!')}")

print(f" {max(7,3,5,8,22,3,19)}") 
print(f" {min(7,3,5,8,22,3,19)}") 

print("=============Random (Używanie bibliotek)==============")

import random as p
print(f" {p.randint(0, 10)}")
print(f" {p.randint(5, 15)}")

print("============= Math (Używanie bibliotek)==============")

import math
print(f"{math.sqrt(16)}")
print(f"{math.ceil(6.7)}")  
print(f" {math.floor(6.7)}")

print("===============Zadania dodatkowe===============")
# Pobierz od użytkownika liczbę, a następnie wartość procentową.
# Program ma za zadanie wyświetlić ile to jest ( % z liczby )
print("=============Procenty==============")


# Pobierz od użytkownika bok sześcianu i oblicz jego objętość oraz pole powierzchni ścian
print("=============Sześcian==============")


# Pobierz ilość osób i komputerów. Oblicz ile średnio przypada komputerów na osobę
print("=============Komputery==============")


# Pobierz promień od użytkownika. Oblicz pole i obwód koła. Dodatkowo oblicz objętość kuli o tym samym promieniu
print("=============Koło i kula==============")

# Masz urodziny i rozdajesz w klasie kolegom cukierki. 
# W siatce masz 234 cukierków, w klasie jest 9 koleżanek i 6  kolegów. 
# Oblicz po ile cukierków możesz maksymalnie rozdać oraz ile cukierków ci zostanie.
print("=============Cukierki==============")
