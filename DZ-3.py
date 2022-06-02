def while1():
    x = int(input('Введи любое число: '))
    while x != 0:
        x = int(input('Введи любое число: '))
        if x == 0:
            break
# print (while1())


def while2():
    x = 5
    while x < 51:
        print(x)
        x = x + 1
# print (while2())

def while3():
    temp = []
    active = True
    while active:
        temp.append(float(input("введи температуру воздуха: ")))
        for t in temp:
            if t >= 22:
                active = False
    print((len(temp)-1)//7)
# print(while3())

def while4():
    x = int(input('Введи любое число: '))
    fibonachi = [1, 1]
    while fibonachi[-1] < x:
        fibonachi.append(fibonachi[-1] + fibonachi[-2])
    fibonachi.pop()
    print(fibonachi)
# print(while4())

def while5():
    x = 0
    print(x)
    while x < 100:
        x = x+5
        print(x)
# print(while5())

def while6():
    numbers = []
    x = float(input('Введи любое число: '))
    numbers.append(x)
    while x != 0:
        x = float(input('Введи любое число: '))
        numbers.append(x)
    print(sum(numbers)/(len(numbers)-1))
# print(while6())

def while7():
    price = [int(input("напиши стоимость товара: "))]
    while price.count(-1) == False:
        price.append(int(input("напиши стоимость следующего товара или '-1', если товаров больше нет: ")))
    price.pop()
    price_new = []
    for p in price:
        if p <= 1500:
            price_new.append(p)
        if p > 1500:
            price_new.append(p*0.92)
    print(sum(price_new))
# print(while7())
# почему не сохраняет список с изменённым значением? - надо создать пустой список и заносить в него новые значения

def for1():
    a = list(range(16))
    b = list(range(7, 19))
    print(a)
    print(b)
# print(for1())

def for2():
    a = list(range(-5, 8))
    b = a.reverse()
    print(a[::2])
# print(for2())

def ooo():
    active = True
    numbers = []
    while active:
        numbers.append(int(input("введи число: ")))
        if numbers.count(-1):
            active = False
    numbers.pop()
    print(numbers)
# print(ooo())

# def for3():
#     numbers = [1, 45, 36, 32, 6, 7, 9, 10, 12, 3, 5, 6, 31, -3, 7, 4]
#     x = 0
#     for n in numbers:
#         if n < ????????:
#             x = x + 1
#     print(x)
# print(for3())



def for4():
    a = str(input("введи текст: "))
    b = list(a)
    for element in b:
        if b.count(element) == 1:
            print(element, end='')
# print(for4())


def for5():
    simbols = str("b22%2mZUk$hv3^b^3s85Q#")
    letters = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = str("0123456789")
    simbols2 = []
    for i in simbols:
        if i in letters:
            simbols2.append("1")
        elif i in numbers:
            simbols2.append("2")
        else:
            simbols2.append("3")
    print("".join(simbols2))
print(for5())





