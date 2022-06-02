# Создать 5 классов:
#
# --- МАТЕРИЯ (имеет атрибуты класса (номер вселенной, закон), а также статический метод, который
# выводит следующую строку: я вселенная номер «значение», я имею закон «значение», дополнительно создать два метода
# экземпляра, через которые можно поменять атрибуты класса (не экземпляра!!!) номер вселенной и закон),
# --- ЧЕЛОВЕК,
# --- МАШИНА,
# --- ЖИВОТНОЕ (на выбор),
# --- КОМПЬЮТЕР.
#
# В каждом из последних четырёх классов должно быть:
#
# один метод класса, который позволяет создать экземпляр класса через другое значение одного из атрибутов
# (то есть в метод передаются одни значения, а экземпляр создаётся уже с преобразованными,
# как на занятии был пример с возрастом и годом рождения),
#
# 3 атрибута экземпляра,
#
# 1 закрытый атрибут экземпляра (для него прописать сетер и гетер),
#
# 3 метода экзепляра класса, в которых используются атрибуты экземпляров класса и атрибуты  класса,
#
# 2 атрибута класса,
#
# а также 2 статических метода, в которых используются атрибуты.
#
# Последние 4 класса должны наследоваться от первого (МАТЕРИЯ).
#
# Также, для последних 4 классов создать счетчик количества экземпляров, которые созданы в классе.

class Materia():

    universe_number = 5
    law = "равноценного обмена"

    @staticmethod
    def text():
        print(f'я вселенная номер {universe_number}, я имею закон {law}.')

    def change_universe_number(self, new_number):
       self.universe_number = new_number

    def change_law(self, new_law):
        self.law = new_law



class Human(Materia):

    civilization = "people"
    year = 2022
    count_exemplar = 0

    def __init__(self, name, hight, age): # метод чего?
        self.name = name
        self.hight = hight
        self.__age = age
        self.nationality = 'zulus'
        self.gender = 'female'
        self.education = 'student'
        Human.count_exemplar += 1

    @classmethod # метод класса
    def func(cls, name, hight):
        return cls(name, f'{hight} cm')

    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age

    def hight_info_female(self):
        print(f'Рост {self.name} на {self.hight - 170} отличается от среднего роста национальности {self.nationality} '
              f'{self.gender} пола. Средний рост равен 170 см по данным на {Human.year} год.')

    def hight_info_male(self):
        self.gender = "male"
        print(f'Рост {self.name} на {self.hight - 175} отличается от среднего роста {self.nationality} национальности '
              f'{self.gender} пола. Средний рост равен 175 см по данным на {Human.year} год.')

    def basic_info(self):
        print(f'Основные сведения по состоянию на {Human.year} год: имя - {self.name}, цивилизация - {Human.civilization}, '
              f'образование - {self.education}, возраст = {Human.get_age(self)}.')

    # @staticmethod
    # def change_status_education():
    #     self.education = input("введите статус образования: ") # ??? NameError: name 'self' is not defined
    #
    # @staticmethod
    # def change_nationality():
    #     self.nationality = input("введите новую национальность: ") # ??? NameError: name 'self' is not defined


vera = Human("Vera", 169, 19)
# alex.change_status_education()   # ??? NameError: name 'self' is not defined
print(vera.basic_info())

itan = Human("Itan", 180, 20)
# vera.change_nationality()   # ??? NameError: name 'self' is not defined
print(itan.hight_info_male())

# print(Human.func(Human, "Sveta", 164)) # ??? TypeError: func() takes 3 positional arguments but 4 were given


class Car(Materia):

    exporter = "France"
    importer = "China"
    brand = "Renault"
    count_exemplar = 0

    def __init__(self, model, color, year, transmission, delivery_date, order_number, dollar_value):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.delivery_date = delivery_date
        self.__order_number = order_number
        self.dollar_value = dollar_value
        # Car.count_exemplar += 1   #  ???  TypeError: unsupported operand type(s) for +=: 'function' and 'int'


    @classmethod
    def euro_value(cls, brand, model, dollar_value):
        return cls(brand, model, (dollar_value * 0.941620) )

    def set_order_number(self, order_number):
        self.__order_number = order_number

    def get_order_number(self):
        return self.__order_number

    def info(self):
        print(f'{Car.brand} {self.model} цвета {self.color} доставили из {Car.exporter} в {Car.importer} {self.delivery_date}.')

    def status(self, status):
        self.status = status
        print(f'Статус доставки заказа №{Car.get_order_number(self)} авто {Car.brand} {self.model} = {self.status}')

    def new_order(self):
        print(f'Получен заказ на авто: {Car.brand} {self.model} {self.year} года, цвет = {self.color}, '
              f'КПП = {self.transmission}. Номер заказа = {Car.get_order_number(self)}.')

    @staticmethod
    def count_exemplar():
        print(Car.count_exemplar)

    # @staticmethod
    # def discount():
    #     disc = input("Назначьте размер скидки от 1 до 100: ")
    #     new_price = dollar_value * (1 - (disc / 100)
    #     print(f"На авто {Car.brand} {model} цвета {color} действует скидка! Цена со скидкой = {new_price}.") # ??? SyntaxError: invalid syntax


auto1 = Car("DUSTER", "orange", 2021, "automatic", "05.05.2022", 1564, 35250)
print(auto1.get_order_number())

auto2 = Car("KAPTUR", "yellow", 2018, "mechanic", "15.02.2022", 1435, 34780)

# print(auto5.euro_value(Car, "Renault", "STEPWAY", 40000)) # ??? TypeError: euro_value() takes 4 positional arguments but 5 were given

auto3 = Car("ARKANA", "silver", 2022, "mechanic", "12.04.2022", 1684, 41350)
auto3.info()
auto3.status("в пути")
auto3.new_order()

auto4 = Car("KOLEOS", "black", 2020, "automatic", "26.06.2022", 1732, 50750)
# auto4.discount()



# class Bird():
#
#
# class Computer():












