import random


# # zad 2
# tab = ["g","o","o","g","l","e"]
# print(tab[::-1])
# a = []
# n = int(input("Number of elements in array:"))
# for i in range(0,n):
#    l = str(input())
#    a.append(l)
# print(a)
# print(a[::-1])

# #zad 3
# # b = []
# # n1 = random.randint(2,11)
# # for i in range(0,n1):
# #     los = random.randint(-5,5)
# #     b.append(los)
# # print(b)

# size = 10
# array = [random.uniform(-5, 5) for _ in range(size)]

# with open("result2.txt", "w") as file:
#     for value in array:
#         file.write(str(value) + "\n")


#zad 4
# def kwad():
#     tab2 = [[0 for x in range(5)] for y in range(5)]
#     #print(tab2)
#     # tab2[0] = [2,3,4,5,6]
#     # print(tab2)
#     for j in range(5):
#         tab2[0][j] = j + 2
#     for i in range(1,5):
#         for j in range(5):
#             tab2[i][j] = tab2[i-1][j]**2
#     print(tab2)
# print(kwad())

#zad5
def histogram(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

        histogram_dict = {}
        for char in text:
            if char in histogram_dict:
                histogram_dict[char] += 1
            else:
                histogram_dict[char] = 1

        return histogram_dict
    
print(histogram("text.txt"))

#zad6
import random

def deck():
    # Tworzenie tali kart
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    suits = ['c', 'd', 'h', 's']
    deck = [(rank, suit) for suit in suits for rank in ranks]

    return deck

def shuffle_deck(deck):
    # Tasowanie talii kart
    random.shuffle(deck)

    return deck

def deal(deck, n):
    # Rozdanie kart graczom
    hands = [deck[i:i+5] for i in range(0, n*5, 5)]

    return hands

my_deck = deck()
print(my_deck)

shuffled_deck = shuffle_deck(my_deck)
print(shuffled_deck)

hands = deal(shuffled_deck, 4)
print(hands)

