# Завдання 6

# Використовуючи код example_10, створіть декоратори @ classmethod для формування переліку
# об'єктів, які підрахують кількість повнолітніх людей в Україні та Америці.

from datetime import date


class MyClass1:
    adults_ukraine = 0  
    adults_usa = 0     

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

        if MyClass1.is_adult_ukraine(age):
            MyClass1.adults_ukraine += 1
        if MyClass1.is_adult_usa(age):
            MyClass1.adults_usa += 1

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    def print_info(self):
        print(f"{self.surname} {self.name}'s age is: {self.age}")

    @staticmethod
    def is_adult_ukraine(age):
        return age >= 18

    @staticmethod
    def is_adult_usa(age):
        return age >= 21

    @classmethod
    def count_adults_ukraine(cls):
        return cls.adults_ukraine

    @classmethod
    def count_adults_usa(cls):
        return cls.adults_usa


person1 = MyClass1('Ivanenko', 'Ivan', 19)
person2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2000)
person3 = MyClass1.fromBirthYear('Sydorchuk', 'Petro', 2010)  

person1.print_info()
person2.print_info()
person3.print_info()

print(f"Кількість повнолітніх людей в Україні: {
      MyClass1.count_adults_ukraine()}")
print(f"Кількість повнолітніх людей в США: {MyClass1.count_adults_usa()}")

