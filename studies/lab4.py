#zad2
def my_func(f, arg):
    return (f(arg))

def func2(x):
    for i in range(x):
        print(my_func(lambda x: x ** 2, i + 1))
func2(4)


# #zad3
tab = [1, 2, 3, 5, 8, 3, 0, 7]
filtered = list(filter(lambda x: x <= 4, tab))
print(filtered)

#zad4
def generate_list():
    string = 'spam'
    for i in range(1, len(string)+1):
        yield string[:i]
print(list(generate_list()))


#zad5
def func5(x):
    return 5*(x**2) + 3*x + 8

def decorator(func):
    def wrapper(x):
        equ= f"5*(x**2) + 3*x + 8 = {func(x)}"
        return equ
    return wrapper

xe = int(input(("Podaj x: ")))
print("dla x = "  + str(xe) + " funcja wyglada nastepujaco:" )

decorEqu = decorator(func5)
print(decorEqu(xe))


#zad6
def Newton(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return n / k * Newton(n - 1, k - 1)

print(Newton(5,3))

#zad7
def test_set():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    
    # Suma zbiorów
    set_union = set1 | set2
    print("Suma zbiorów:", set_union)
    
    # Część wspólna zbiorów
    set_intersection = set1 & set2
    print("Część wspólna zbiorów:", set_intersection)
    
    # Różnica zbiorów
    set_difference = set1 - set2
    print("Różnica zbiorów:", set_difference)
    
    # Różnica symetryczna zbiorów
    set_symmetric_difference = set1 ^ set2
    print("Różnica symetryczna zbiorów:", set_symmetric_difference)
    
    # Dodanie elementu do zbioru
    set1.add(6)
    print("Dodanie elementu do zbioru:", set1)
    
    # Usunięcie elementu ze zbioru
    set1.remove(6)
    print("Usunięcie elementu ze zbioru:", set1)
    
    # Usunięcie losowego elementu ze zbioru
    set1.pop()
    print("Usunięcie losowego elementu ze zbioru:", set1)
    
    # Sprawdzenie czy element należy do zbioru
    if 2 in set1:
        print("2 jest elementem zbioru set1")
    else:
        print("2 nie jest elementem zbioru set1")
    
    # Sprawdzenie ilości elementów w zbiorze
    print("Liczba elementów w zbiorze:", len(set1))

test_set()