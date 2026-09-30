# Przypomnienie poprzedniej lekcji

print("=============Powtórka==============")
imie = "Jan"
nazwisko = "Kowalski"
wiek = int(input("Podaj swój wiek: "))  # zczytywanie wieku użytkownika jako liczba całkowita
wzrost = 1.77

print(f'{imie} {nazwisko}, {wiek} lat, {wzrost}m wzrostu')

print(f'{imie}: {type(imie)}')
print(f'{nazwisko}: {type(nazwisko)}')
print(f'{wiek}: {type(wiek)}')
print(f'{wzrost}: {type(wzrost)}')

# TODO : zczytaj i wypisz od użytkownika jego wzrost i przypisz go do zmiennej wzrost. Pamiętaj, że wzrost jest liczbą zmiennoprzecinkową (float).
print("=============Wczytywanie wzrostu==============")


# TODO : użyj try catch aby obsłużyć sytuację, gdy użytkownik poda niepoprawną wartość wzrostu (np. tekst zamiast liczby). 
# W przypadku błędu wypisz komunikat o błędzie i przypisz zmiennej wzrost wartość 0.0. 
# Jeśli użytkownik poda poprawną wartość, przypisz ją do zmiennej wzrost i wypisz komunikat o poprawnym wczytaniu wzrostu i wypisz typ i wartość zmiennej wzrost.
print("=============Obsługa błędów==============")
# try:

# except:



# TODO: napisz równanie, którego wynikiem jest liczba zmiennoprzecinkowa (float) i wypisz wynik oraz typ zmiennej
print("=============Równanie==============")


# TODO: policz średnią ocen
print("=============Średnia ocen==============")

# matematyka = int(input("Podaj ocenę z matematyki: "))
# fizyka = int(input("Podaj ocenę z fizyki: "))
# polski = int(input("Podaj ocenę z polskiego: "))
# ang = int(input("Podaj ocenę z angielskiego: "))

srednia = 0 #usun zero i przypisz srednia ocen

print(f"Średnia: {srednia}")
print(f"Typ: {type(srednia)}")


# TODO: użyj operatora floor division (//) aby policzyć ile pełnych paczek kabla można zrobić z podanej długości kabla. Wypisz wynik oraz typ zmiennej.


dlugosc_kabla = 767   # float
dlugosc_paczki = 10   # int

liczba_paczek = 0 #usun zero i przypisz wynik dzielenia długości kabla przez długość paczki (floor division)

print(f"Ilość kabla (float): {dlugosc_kabla} m")
print(f"Liczba PEŁNYCH paczek (int): {liczba_paczek}")


# konwersja typów zmiennych. Co się dzieje, gdy konwertujemy float na int? Sprawdźmy to.


x = int(6.7)
print(f'{x}: {type(x)}')


# TODO: użyj operatora modulo (%) aby policzyć ile kabli zostanie po zrobieniu pełnych paczek. Wypisz wynik oraz typ zmiennej.


reszta = dlugosc_kabla - liczba_paczek * dlugosc_paczki
print(f"Pozostało {reszta} metrów kabla") # oczekiwany wynik


# Potęgowanie w Pythonie odbywa się za pomocą operatora **. 
# TODO: Zczytaj od użytkownika liczbę i potęgę, a następnie wypisz wynik potęgowania oraz typ zmiennej.



# Rounding liczb zmiennoprzecinkowych w Pythonie odbywa się za pomocą funkcji round(). Co to znaczy rounding?
print("=============funckje wbudowane==============")

print(round(6.7))  

print(abs(-10))

print(len("Hello world!")) 

print(max(7,3,5,8,22,3,19)) 
print(min(7,3,5,8,22,3,19)) 

print("=============Random (Używanie bibliotek)==============")

import random as random
print(random.randint(0, 10))
print(random.randint(5, 15))

print("============= Math (Używanie bibliotek)==============")

import math
print(math.sqrt(16))
print(math.ceil(6.7))  
print(math.floor(6.7))

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