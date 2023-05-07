from datetime import date
#zad1
x = 2
y = 3
print("liczba x to " + str(x) + " liczba y to " + str(y))
print("suma: ", x+y)
print("różnica: ", x-y)
print("mnożenie: ", x*y)
print("dzielenie: ", x/y)

#zad2
# print("Podaj imie: ")
# name = input()
# print("Witaj " +name)

#zad3
# print("Podaj dwie liczby, aby otrzymac sume: ")
# print(float(int(input())+int(input())))

#zad4
print(sum(range(8,81)))

#zad5
print(date.fromisoformat("2023-06-06")-date.today())

# print("podaj date w postaci rok-miesiac-dzien")
# data = int(input()).split("-")
# akt_data = date.today()
# print(data - akt_data)

print("Podaj liczbe pierwsza:")
x = int(input())
print("Podaj liczbe drugą:")
y = int(input())
print("Wybierz opcje wybierając 1 dla +, 2 dla -, 3 dla *, 4 dla /'")
w = int(input())
if (w == 1):
    print("suma: ", x+y)
elif (w == 2):
    print("różnica: ", x - y)
elif (w == 3):
    print("mnożenie: ", x*y)
else: print("dzielenie: ", x/y)