import random
from functools import reduce

# L_1 = lambda film, cinema, time: print("Билета на " + film + " в " + cinema + " на " + time + " забронирован.")
# L_1(Покахонтас, Центральный, восемь)

def smallest_2(a, b, c):
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    else:
        print(c)
# smallest(8.2,9,3.1)

L_3 = lambda earth_years: print((earth_years*365)/687)
# L2(4)

def get_random_array_4(n=10):
    print(random.sample(range(50), n))
# get_random_array(5)

def sum_of_digits_5(number):
    a = str(number)
    b = list(a)
    numbers = []
    for c in b:
        c = int(c)
        numbers.append(c)
    def sum_numbers(first, second):
        return (first + second)
    result = reduce(sum_numbers, numbers)
    print(result)
# sum_of_digits_5(64577)

def factorial_6(n):
    a = list(range(1,n+1))
    def multiply(first, second):
        return (first * second)
    result = reduce(multiply, a)
    print(result)
# factorial_6(7)

def average_7():
    numbers = []
    print("Введи число или 'stop' для завершения списка: ")
    x = input()
    while x != 'stop':
        numbers.append(int(x))
        print("Введи число или 'stop' для завершения списка: ")
        x = input()
    print(sum(numbers)/len(numbers))
# average_7()