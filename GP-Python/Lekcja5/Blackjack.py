import random

karty = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "J", "Q", "K", "A"
]


def wartosc_karty(karta):
    match karta:
        case "J":
            return 10
        case "Q":
            return 10
        case "K":
            return 10
        case "A":
            return 11
        case _:
            return int(karta)


def suma_kart(reka):
    suma = 0
    liczba_asow = 0

    for karta in reka:
        suma += wartosc_karty(karta)

        if karta == "A":
            liczba_asow += 1

    while suma > 21 and liczba_asow > 0:
        suma -= 10
        liczba_asow -= 1

    return suma


gracz = []
krupier = []

gracz.append(random.choice(karty))
gracz.append(random.choice(karty))

krupier.append(random.choice(karty))
krupier.append(random.choice(karty))


print("=== BLACKJACK ===")

print("Twoje karty:", gracz)
print("Twoja suma:", suma_kart(gracz))

print("Jedna karta krupiera:", krupier[0])


# sprawdzamy blackjacka gracza
if len(gracz) == 2 and suma_kart(gracz) == 21:
    print("BLACKJACK! Automatycznie wygrywasz!")

else:

    # tura gracza
    while suma_kart(gracz) < 21:

        wybor = input("Dobierasz karte? tak/nie: ")

        if wybor == "tak":
            nowa_karta = random.choice(karty)
            gracz.append(nowa_karta)

            print("Dobrales:", nowa_karta)
            print("Twoje karty:", gracz)
            print("Twoja suma:", suma_kart(gracz))

        elif wybor == "nie":
            break

        else:
            print("Wpisz tak albo nie")


    # sprawdzamy czy gracz przekroczyl 21
    if suma_kart(gracz) > 21:
        print("Przekroczyles 21. Przegrywasz.")

    else:

        # tura krupiera
        print("\nKarty krupiera:", krupier)
        print("Suma krupiera:", suma_kart(krupier))

        while suma_kart(krupier) < 17:
            nowa_karta = random.choice(karty)
            krupier.append(nowa_karta)

            print("Krupier dobiera:", nowa_karta)
            print("Karty krupiera:", krupier)
            print("Suma krupiera:", suma_kart(krupier))


        suma_gracza = suma_kart(gracz)
        suma_krupiera = suma_kart(krupier)

        print("\n=== WYNIK ===")

        if suma_krupiera > 21:
            print("Krupier przekroczyl 21. Wygrywasz!")

        elif suma_gracza > suma_krupiera:
            print("Wygrywasz!")

        elif suma_gracza < suma_krupiera:
            print("Przegrywasz.")

        else:
            print("Remis.")