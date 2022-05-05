def conversion1():
    inches = float(input("Введи дюймы: "))
    centimeters = inches * 2.54
    print(centimeters, "см")
# conversion1()

# def conversion1(inches):
#     inches = float
#     centimeters = inches * 2.54
#     print(centimeters)
# conversion1("5")
# почему так не получается?

def conversion2():
    centimeters = float(input("Введи сантиметры: "))
    inches = centimeters / 2.54
    print(inches, "дюйма")
# conversion2()

def conversion3():
    miles = float(input("Введи мили: "))
    kilometers = miles * 1.609
    print(kilometers, "км")
# conversion3()

def conversion4():
    kilometers = float(input("Введи километры: "))
    miles = kilometers / 1.609
    print(miles, "мили")
# conversion4()

def conversion5():
    pounds = float(input("Введи фунты: "))
    kilograms = pounds / 2.205
    print(kilograms, "кг")
# conversion5()

def conversion6():
    kilograms = float(input("Введи килограммы: "))
    pounds = kilograms * 2.205
    print(pounds, "фунта")
# conversion6()

def conversion7():
    ounces = float(input("Введи унции: "))
    grams = ounces * 28.35
    print(grams, "гр")
# conversion7()

def conversion8():
    grams = float(input("Введи граммы: "))
    ounces = grams / 28.35
    print(ounces, "унции")
# conversion8()

def conversion9():
    gallon = float(input("Введи галлоны: "))
    liters = gallon * 3.785
    print(liters, "литра")
# conversion9()

def conversion10():
    liters = float(input("Введи литры: "))
    gallons = liters / 3.785
    print(gallons, "галлона")
# conversion10()

def conversion11():
    pints = float(input("Введи пинты: "))
    liters = pints / 2.113
    print(liters, "литра")
# conversion11()

def conversion12():
    liters = float(input("Введи литры: "))
    pints = liters * 2.113
    print(pints, "пинты")
# conversion12()

def converter():
    x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
    while x != 0:
        if x == 1:
            conversion1()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 2:
            conversion2()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 3:
            conversion3()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 4:
            conversion4()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 5:
            conversion5()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 6:
            conversion6()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 7:
            conversion7()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 8:
            conversion8()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 9:
            conversion9()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 10:
            conversion10()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 11:
            conversion11()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x == 12:
            conversion12()
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
        elif x > 12 or x < 0:
            print("wrong number")
            x = int(input("Choose from 1 to 12, print '0' to stop the program: "))
    print("exit")
# converter()

# def fun2():
#     m = int(input("Введи 1ое целое число: "))
#     n = int(input("Введи 2ое целое число: "))
#     numbers = list(range(m, n))
#     den = list(range(2, n-1))
#     x = []
#     for n in numbers:
#         while n % ??? == 0:
#             x.append(???)
#     print(x)
# print(fun2())


def fun2():
    m = int(input("Введи 1ое целое число: "))
    n = int(input("Введи 2ое целое число: "))
    for i in range(m, n+1):
        y = []
        for x in range(0, i):
            if i % x == 0:
                y.append(x)
    print(y)
print(fun2())