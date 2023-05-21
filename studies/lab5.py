#zad2,3,4
class Osoba:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Student(Osoba):
    def __init__(self, name, surname, albumNum):
        super().__init__(name, surname)
        self.albumNum = albumNum

    def __str__(self):
        return "Czesc! Jestem " + self.name + " " + self.surname + " a moj numer albumu to " + str(self.albumNum) + "."

st1 = Student("Mario", "Super", 135790)
st2 = Student("Henryk", "Kociołek", 124578)
st3 = Student("Jan", "Dzban", 135679)

print(st1)
print(st2)
print(st3)

#zad5
class Liczba:
    def __init__(self, liczba):
        self.liczba = liczba

    def __add__(self, other):
        x = self.liczba
        y = other.liczba
        wynik = x ** 2 + 2 * x * y + y
        return Liczba(wynik)

l1 = Liczba(3)
l2 = Liczba(4)

wynik = l1 + l2
print(wynik.liczba) 

#zad6
class Dog:
    count = 0  # this is a class variable
    dogs = []  # this is a class variable

    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def print_dog_info():
        print("ilość psów: {}".format(Dog.count))
        print("Imiona psów:")
        for dog in Dog.dogs:
            print(dog)

# Przykładowe użycie
dog1 = Dog("Burek")
dog2 = Dog("Azor")

dog1.bark(3)
dog2.bark(2)

Dog.print_dog_info()

#zad7
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        self._pineapple_allowed = value


pizza = Pizza(["cheese", "ham"])
print(pizza.pineapple_allowed)  # False

pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)  # True
