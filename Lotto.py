from totomodul import ustawienia, losujliczby, wyniki, pobierztypy
from totomodul import czytaj_json , zapisz_json
import time

def main(args):
    # ustawienia gry
    nick, ileliczb, maksliczba, ilerazy = ustawienia()

    # losujemy liczby
    liczby = losujliczby(ileliczb, maksliczba)

    # pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)

        ileTraf = wyniki(set(liczby),typy)
    
    nazwapliku = nick + ".json" #historia losowan
    losowania = czytaj_json(nazwapliku)
    #losowania = czytaj_str(nazwapliku)

    losowania.append({
        "czas": time.time(),
        "dane": (ileliczb, maksliczba),
        "wylosowane": liczby,
        "ile": ileTraf
    })

    zapisz_json(nazwapliku, losowania)

    print("Wylosowane liczby:", liczby)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
