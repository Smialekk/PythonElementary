import random
import math

#zad2
def lotto():
    numbers = []
    while len(numbers) < 6:
        number = random.randint(1, 49)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)
print(lotto())

#zad3, zad4, zad6

def save_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")

# def dodaj(x,y):
#     return x + y
# def odejmownie(x,y):
#     return x - y
# def mnozenie(x,y):
#     return x * y
# def dziel(x,y):
#     return x / y

# def obwKola(r):
#     return math.pi*2*r
# def polekola(r):
#     return math.pi*r*r

# print("Podaj liczbe pierwsza:")
# x = int(input())
# print("Podaj liczbe drugą:")
# y = int(input())
# print("Wybierz opcje wybierając 1 dla +, 2 dla -, 3 dla *, 4 dla / , 5 -> obw kola, 6 -> pole koła")
# w = int(input())
# if (w == 1):
#     print("suma: ", dodaj(x,y))
# elif (w == 2):
#     print("różnica: ", odejmownie(x,y))
# elif (w == 3):
#     print("mnożenie: ", mnozenie(x,y))
# elif (w == 4): 
#     if y == 0: 
#         print("Nie dziel przez 0 cho") 
#     print("dzielenie: ", dziel(x,y))
# elif (w == 5):
#     print("Podaj promien kola:")
#     r = int(input())
#     print("Obwód kola wynosi: ", obwKola(r))
#     data = f"Promień: {r:.2f}, Obwód: {obwKola(r):.2f}"
# elif (w == 6):
#     print("Podaj promien kola:")
#     r = int(input())
#     print("Pole kola wynosi: ", polekola(r))
#     data = f"Promień: {r:.2f}, Pole: {polekola(r):.2f}"
# else: print("Zly wybor")
# save_to_file("kalkulator.txt", data)




#zad5
print("\n")
def sumaListy(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s

def read_numbers_from_file(filename, sumaListy):
    with open(filename, "r") as f:
        numbers = [int(line.strip()) for line in f]
    return sumaListy(numbers)

filename = "numbers.txt" #{5 ,6 ,7, 1} kazda w nowej lini
result = read_numbers_from_file(filename, sumaListy)
print(result)

#zad7
print("Rozwiązywnie równania kwadratowego")
a = int(input("Podaj współczynnik a: "))
b = int(input("Podaj współczynnik b: "))
c = int(input("Podaj współczynnik c: "))
if a == 0:
    print("Równanie liniowe postaci "+ str(b)+"x + " + str(c))
    xl = -c/b
    data7 = f"Równanie liniowe postaci {b:.2f}x + {c:.2f}, rozwiazanie x= {xl:.2f}"
else:
    print("Równanie kwadratowe postaci "+ str(a)+"x^2 + " + str(b)+"x + " + str(c))
    data7 = f"Równanie kwadratowe postaci {a:.2f}x^2 + {b:.2f}x + {c:.2f}"
    delta = b*b - 4*a*c
    if delta < 0:
        print("Brak rozwiązań w zbiorze R")
        data7 = f"Równanie kwadratowe postaci {a:.2f}x^2 + {b:.2f}x + {c:.2f} Brak rozwiązań w zbiorze R"
    else:
        if delta == 0:
            x0 = -b/(2*a)
            print("Jedno rozwiązanie równe: "+ str(x0))
            data7 = f"Równanie kwadratowe postaci {a:.2f}x^2 + {b:.2f}x + {c:.2f} Jedno rozwiązanie równe: {x0:.2f}"
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("Dwa rozwiązania x1: "+ str(x1)+ " oraz x2: "+ str(x2))
            data7 = f"Równanie kwadratowe postaci {a:.2f}x^2 + {b:.2f}x + {c:.2f} Dwa rozwiązania x1: {x1:.2f} + x2: {x2:.2f}"
save_to_file("result.txt", data7)
            