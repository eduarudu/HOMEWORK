# def password():
#     pass1 = input("Введи пароль: ")
#     pass2 = input("Повтори пароль для подтверждения: ")
#     x = False
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     symbols = ['%', '@', '#', '$', '&', '*', '!', '~']
#     while x == False:
#         if "123"  in pass1 or "password" in pass1:
#             print("Простой!")
#             pass1 = input("Введи пароль: ")
#             pass2 = input("Повтори пароль для подтверждения: ")
#             continue
#         if pass1 != pass2:
#             print("Различаются")
#             pass1 = input("Введи пароль: ")
#             pass2 = input("Повтори пароль для подтверждения: ")
#             continue
#         else:
#             for i in pass1:
#                 if i in numbers >= 3 and i in letters >= 3 and i in symbols >= 1 and pass1.lower() != pass1 and len(pass1) >= 12:
#                     print("OK")
#             x = True
#             break
#         print("Такой пароль не подходит.")
#         pass1 = input("Введи пароль: ")
#         pass2 = input("Повтори пароль для подтверждения: ")
# password()

def equate(a, b):
    print((a+4*b)*(a-3*b)+a)
# equate(5,3)

# def scrabble(word1):
#     letters = {
#         'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3,
#         'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5,'J':8, ' X':8, 'Q':10, 'Z':10, 'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1,
#         'О':1, 'Р':1, 'С':1, 'Т':1, 'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2, 'Б':3, 'Г':3, 'Ё':3, 'Ь':3, 'Я':3, 'Й':4,
#         'Ы':4, 'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5, 'Ш':8, 'Э':8, 'Ю':8, 'Ф':10, 'Щ':10, 'Ъ':10
#         }
#     numbers = []
#     for i in word1:
#        if i in letters.keys():
#            numbers.append(letters.values()) #как указать, что нужно добавить значение именно этого ключа?
#     print(sum(numbers))
# scrabble('CAT')

def email():
    emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
              'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
              'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}



