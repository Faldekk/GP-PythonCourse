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
wzrost = float(input("Podaj swój wzrost: "))
print(f"wzrost: {wzrost} typ wzrostu: {type(wzrost)}")

# TODO : użyj try catch aby obsłużyć sytuację, gdy użytkownik poda niepoprawną 
# wartość wzrostu (np. tekst zamiast liczby). 
# W przypadku błędu wypisz komunikat o błędzie i przypisz zmiennej wzrost wartość 0.0. 
# Jeśli użytkownik poda poprawną wartość, przypisz ją do zmiennej wzrost i wypisz komunikat 
# o poprawnym wczytaniu wzrostu i wypisz typ i wartość zmiennej wzrost.

print("=============Obsługa błędów==============")
try:
    wzrost = float(input("Podaj swój wzrost: "))
    print(f"wzrost: {wzrost} typ wzrostu: {type(wzrost)}")
except:
    print("Coś poszło nie tak")


# TODO: napisz równanie, którego wynikiem jest liczba zmiennoprzecinkowa (float) i wypisz wynik oraz typ zmiennej
print("=============Równanie==============")
zmienna1 = 1
zmienna2 = 3
wynik = zmienna1 / zmienna2
print(f'wynik dzielenia: {zmienna1} / {zmienna2} = {wynik}')
# TODO: policz średnią ocen
print("=============Średnia ocen==============")

matematyka = int(input("Podaj ocenę z matematyki: "))
fizyka = int(input("Podaj ocenę z fizyki: "))
polski = int(input("Podaj ocenę z polskiego: "))
ang = int(input("Podaj ocenę z angielskiego: "))

srednia = (matematyka + fizyka + polski + ang) / 4

print(f"Średnia: {srednia}")
print(f"Typ: {type(srednia)}")


# TODO: użyj operatora floor division (//) aby policzyć ile pełnych paczek kabla można zrobić z podanej długości kabla. Wypisz wynik oraz typ zmiennej.
print("=============Podział kabla na paczki==============")

dlugosc_kabla = 767   
dlugosc_paczki = 10   

liczba_paczek = dlugosc_kabla // dlugosc_paczki 

print(f"Ilość kabla (float): {dlugosc_kabla} m")
print(f"Liczba PEŁNYCH paczek (int): {liczba_paczek}")


# konwersja typów zmiennych. Co się dzieje, gdy konwertujemy float na int? Sprawdźmy to.
print("=============Konwersja typów zmiennych==============")

x = int(6.7)
print(f'{x}: {type(x)}')


# TODO: użyj operatora modulo (%) aby policzyć ile kabli zostanie po zrobieniu pełnych paczek. Wypisz wynik oraz typ zmiennej.
print("=============Reszta kabla==============")

reszta = dlugosc_kabla - liczba_paczek * dlugosc_paczki
print(f"Pozostało {reszta} metrów kabla") # oczekiwany wynik

reszta2 = dlugosc_kabla % dlugosc_paczki
print(f"Pozostało {reszta2} metrów kabla")

# Potęgowanie w Pythonie odbywa się za pomocą operatora **. 
# TODO: Zczytaj od użytkownika liczbę i potęgę, a następnie wypisz wynik potęgowania oraz typ zmiennej.
print("=============Potęgowanie==============")
liczba = int(input("Podaj liczbe: "))
potega = int(input("Podaj potege: "))
print(f'{liczba} do potegi {potega} = {liczba ** potega}')
# Rounding liczb zmiennoprzecinkowych w Pythonie odbywa się za pomocą funkcji round(). Co to znaczy rounding?
print("=============funckje wbudowane==============")

print(f"Zaokrąglenie (6.7): {round(6.7)}")

print(f"Wartość bezwzględna: {abs(-10)}")

print(f"Długość słowa albo czegoś: {len('Hello world!')}")

print(f"Wartość maksymalna: {max(7,3,5,8,22,3,19)}") 
print(f"Wartość minimalna: {min(7,3,5,8,22,3,19)}") 

print("=============Random (Używanie bibliotek)==============")

import random as p
print(f"Losowa liczba od 0 do 10: {p.randint(0, 10)}")
print(f"Losowa liczba od 5 do 15: {p.randint(5, 15)}")

print("============= Math (Używanie bibliotek)==============")

import math
print(f"Pierwiastkowanie: {math.sqrt(16)}")
print(f"Zaokrąglenie w górę: {math.ceil(6.7)}")  
print(f"Zaokrąglenie w dół: {math.floor(6.7)}")

print("===============Zadania dodatkowe===============")
# Pobierz od użytkownika liczbę, a następnie wartość procentową.
# Program ma za zadanie wyświetlić ile to jest ( % z liczby )
print("=============Procenty==============")
liczba = int(input("Podaj liczbę: "))
procent = int(input("Podaj %: "))
wynik = (liczba * procent) / 100
print(f'procent wynosi {wynik}')

# Pobierz od użytkownika bok sześcianu i oblicz jego objętość oraz pole powierzchni ścian
print("=============Sześcian==============")
a = int(input("Długość boku sześcianu: "))
objetosc = a ** 3 
Powierzchnia = (a ** 2 ) * 6

# Pobierz ilość osób i komputerów. Oblicz ile średnio przypada komputerów na osobę
print("=============Komputery==============")
osob = int(input("Podaj ilość osób: "))
komp = int(input("Podaj ilość komputerów: "))
komp_na_os = komp / osob
print(f"Przypada średnio {komp_na_os} komputerów na osobę")

# Pobierz promień od użytkownika. Oblicz pole i obwód koła. Dodatkowo oblicz objętość kuli o tym samym promieniu
print("=============Koło i kula==============")
osob = int(input("Podaj ilość osób: "))
komp = int(input("Podaj ilość komputerów: "))
komp_na_os = komp / osob
print(f"Przypada średnio {komp_na_os} komputerów na osobę")

# Masz urodziny i rozdajesz w klasie kolegom cukierki. 
# W siatce masz 234 cukierków, w klasie jest 9 koleżanek i 6  kolegów. 
# Oblicz po ile cukierków możesz maksymalnie rozdać oraz ile cukierków ci zostanie.
print("=============Cukierki==============")
cukierki = 234
dzieci = 9 + 6

cukierki_na_osobe = cukierki // dzieci
reszta = cukierki % cukierki_na_osobe

print(f"Rozdam po {cukierki_na_osobe} i zostanie mi {reszta} cukierków")
print(f"Rozdałem: {cukierki_na_osobe * dzieci} cukierków")