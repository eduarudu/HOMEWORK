# 1.	Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три атрибута, конструктор, два метода.

class Book():
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def start_reading(self):
        print(f"I started reading '{self.name}' by '{self.author}'.")

    def finish(self):
        print(f"I finished reading '{self.name}' by '{self.author}'.")



 class Triangle():
     def __init__(self, a, b, c):
         self.a = a
         self.b = b
         self.c = c

     def perimeter(self):
         per = self.a + self.b + self.c
         print(f'perimetr = {per}.')

     def square(self):
         per = self.a + self.b + self.c
         sq = (per(per - self.a)(per - self.b)(per - self.c) / 2) ** 0.5
         print(f'square = {sq}.')



class Painting():
    def __init__(self, name, author, paint_type):
        self.name = name
        self.author = author
        self.paint_type = paint_type

    def status(self):
        status = input('введите статус готовности картины: ')
        print(f'статус готовности картины: {status}')

    def price(self):
        price = input('введите стоимость картины: ')
        print(f'цена картины: {price}')


# 2.	Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорость (скорость + 5), уменьшение скорости (скорость - 5),
# стоп (сброс скорости на 0), отображение скорости, разворот (изменение знака скорости).

class Car():
    def __init__(self):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def increase_speed(self):
        self.speed = self.speed + 5

    def speed_reduction(self):
        self.speed = self.speed - 5

    def stop_speed(self):
        self.speed = 0

    def show_speed(self):
        print(f'speed = {speed}')

    def reversal(self):
        self.speed = self.speed * (-1)



# 3.	Создайте класс Doctor, у которого есть следующие атрибуты: специальность, стаж работы, ЗП, место работы,
# место учёбы, квалификация (1, 2, или высшая категория), должность,
# а также методы: do (выводит текст – следую протоколу оказания мед. помощи), work (я работаю в {место работы},
# у меня стаж {стаж работы}). При этом класс Doctor должен наследоваться от класса Human,
# который имеет атрибуты name и age, а также методы say_name (выводит текст «Привет, меня зовут «имя»»)
# и say_age (выводит текст «Мне «возраст» лет»)

class Human()
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print(f'Привет, меня зовут {name}.')

    def say_age(self):
        print(f'Мне {age} лет.')

class Doctor(Human):
    def __init__(self, name, age, speciality, work_experience, salary, work_place, study_place,
                 qualification, position):
        super().__init__(self, name, age)
        self.speciality = speciality
        self.work_experience = work_experience
        self.salary = salary
        self.work_place = work_place
        self.study_place = study_place
        self.qualification = qualification
        self.position = position

    def do(self):
        print("следую протоколу оказания мед. помощи")

    def work(self):
        print(f'я работаю в {study_place}, у меня стаж {work_experience}')

