import json
import random
import os

def ustawienia():
    """Funkcja pobiera ilość losowanych liczb, maksymalną losowaną wartość
    oraz ilość prób. Pozwala określić stopień trudności gry."""
    
    nick = input("Pdoaj nick: ")
    nazwapliku = nick + ".ini"
    gracz = czytaj_ust(nazwapliku)
    odp = None
    if gracz: #jesli jest graacz
        print("Twoje ustawienia: \nLiczb: %s\nZ Maksymalnie: %s\nLosowań: %s" %
            (gracz[1], gracz[2], gracz[3]))
        odp = input("Zmieniasz (t/n)? ")
    
    if not gracz or odp.lower() == "t":
        while True:
            try:
                ileLiczb = int(input("Podaj ilość typowanych liczb: "))
                maksLiczba = int(input("Podaj maksymalną losowaną liczbę: "))
                if ileLiczb > maksLiczba:
                    print("Błędne dane!")
                    continue
                ilelos = int(input("Ile losowań: ")) #'ilerazy' w main
                break
                #return (ileLiczb, maksLiczba, ilelos)
            except ValueError:
                print("Błędne dane!")
                continue
        gracz = [nick, str(ileLiczb), str(maksLiczba), str(ilelos)]
        zapisz_ust(nazwapliku, gracz)
    
    return gracz[0:1] + [int(x) for x in gracz[1:4]]


def czytaj_ust(nazwapliku):
    if os.path.isfile(nazwapliku):
        plik = open(nazwapliku, "r")
        linia = plik.readline()
        plik.close()
        if linia:
            return linia.split(";")
    return False


def zapisz_ust(nazwapliku, gracz):
    plik = open(nazwapliku, "w")
    plik.write(";".join(gracz))
    plik.close()


def losujliczby(ileLiczb, maksLiczba):
    """Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks"""
    liczby = []
    i = 0
    while i < ileLiczb:
        liczba = random.randint(1, maksLiczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1
    return liczby


def wyniki(liczby,typy):
    """Funkcja porównuje wylosowane i wytypowane liczby,
    zwraca ilość trafień"""
    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))

        trafione = ", ".join(map(str,trafione))
        print("Trafione liczby: %s" % trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

    print("\n" + "x" * 40 + "\n")  # wydrukuj 40 znaków x
    return len(trafione)


def pobierztypy(ileLiczb, maksLiczba):
    """Funkcja pobiera od użytkownika jego typy wylosowanych liczb"""
    print("Wytypuj %s z %s liczb: " % (ileLiczb, maksLiczba))
    typy = set()
    i = 0
    while i < ileLiczb:
        try:
            typ = int(input("Podaj liczbę %s: " % (i + 1)))
        except ValueError:
            print("Błędne dane!")
            continue

        if 0 < typ <= maksLiczba and typ not in typy:
            typy.add(typ)
            i = i + 1
        else:
            print("Błąd, Podaj inną liczbe")
    return typy

    	

def czytaj_json(nazwapliku):
    """Funkcja odczytuje dane w formacie json z pliku"""
    dane = []
    if os.path.isfile(nazwapliku):
        with open(nazwapliku, "r") as plik:
            dane = json.load(plik)
    return dane


def zapisz_json(nazwapliku, dane):
    """Funkcja zapisuje dane w formacie json do pliku"""
    with open(nazwapliku, "w") as plik:
        json.dump(dane, plik)

def zapisz_str(nazwapliku, dane):
    """Funkcja zapisuje dane w formacie txt do pliku"""
    with open(nazwapliku, "w") as plik:
        for slownik in dane:
            linia = [str(k) + ":" + str(w) for k, w in slownik.items()]
            linia = ";".join(linia)
            # plik.write(linia+"\n") – other way
            print >>plik, linia



