# def Золото():
#     s = input("Введите предложение: ")
#     for "золото" in s = True:
#         print("Да")
#         else: print("Нет")
# print(Золото())

def Золото():
    s = input("Введите предложение: ")
    if "золото" in s:                       # if ___ in ___:
        print("Да")
    else:
        print("Нет")
# print(Золото())

def Экзамен():
    student_mark = int(input("Какая у тебя оценка?: "))
    if student_mark <= 40:
        print("Не очень")
    elif student_mark <= 60:
        print("Неплохо")
    elif student_mark <= 80:
        print("Хорошо")
    elif student_mark <= 90:
        print("Отлично")
    else:
        print("Невероятно!")


def Запрос():
    age = int(input("Сколько вам лет?: "))
    if age >= 20:
        print("Вы уверены?")
        answer = input()
        if answer.lower() == "да":
            print("Доступ разрешён!")
        else:
            print("Доступ запрещён.")
    else:
        print("Доступ запрещён.")


def Калькулятор():
    number1 = int(input("Введите 1ое число: "))
    number2 = int(input("Введите 2ое число: "))
    action = str(input("Введите математическую операцию: "))
    if action == '+':
        print(number1 + number2)
    elif action == '-':
        print(number1 - number2)
    elif action == '*':
        print(number1 * number2)
    elif action == '/' and number2 != 0:
        print(number1 / number2)
    else:
        print("error")


def Строки1():
    S = ('Строки на Python')
    S1 = (S * 7)
    S2 = str(S + " " + S1)
    print(S, S1, S2, sep=", ")


def Строки2():
    string = input('Введите значение: ')
    first = string[0]
    last = string[-1]
    print(first, last)


def Строки3_var1():
    string = input('Введите значение: ')
    letter1 = string[0]
    letter_end = string[-1]
    root1 = string.strip(letter1)
    root2 = root1.strip(letter_end)
    new_string = (letter_end + root2 + letter1)
    print(string, new_string)

def Строки3_var2():
    string = input('Введите значение: ')
    new_string = (string[-1] + string[1:-1] + string[0])
    print(string, new_string)
# print(Строки3_var2())

def Строки4():
    input('Введите значение: ')
    new_string = sta[::-1]
    print(string, new_string)


def Строки5():
    string: str = input('Введите три слова через пробел: ')
    txt = string.split(" ")
    print(txt[0].count("а"))
    if txt[1].count("а") <= 0:
        print("error")
    else:
        print(txt[1].replace("а", "А"))
    return


def Строки6():
    passw = input('Введите пароль: ')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    has_letter = False
    has_number = False
    for i in passw:
        if i in letters:
            has_letter = True
        if i in numbers:
            has_number = True
    if (has_letter and has_number and (" " not in passw)):
        print("True")
    else:
        print("False")
print(Строки6())

def Солнечная_система():
    solar_system = {'Jupiter':1321, 'Mars':0.15, 'Saturn':764}
    print(solar_system)
    solar_system['Mercury'] = 0.05
    solar_system['Venus'] = 0.86
    solar_system['Neptune'] = 57.7
    solar_system['Pluto'] = 0.059
    solar_system['Earth'] = 1
    print(solar_system)

def Больше_не_планета():
    solar_system = {
        'Jupiter': 1321, 'Mars': 0.15, 'Saturn': 764, 'Mercury': 0.05,
        'Venus': 0.86, 'Neptune': 57.7, 'Pluto': 0.059, 'Earth': 1
        }
    print(solar_system)
    solar_system.pop('Pluto')
    print(solar_system)
# print(Больше_не_планета())
