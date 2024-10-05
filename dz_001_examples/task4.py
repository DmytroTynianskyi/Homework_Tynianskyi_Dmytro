# Завдання 4
# Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів,
# доступних для продажу, і функцію продажу заданого автомобіля.

class Car:
    def __init__(self, make, model, year, price):
        self.make = make  
        self.model = model 
        self.year = year  
        self.price = price  

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, price={self.price})"

    def __str__(self):
        return f"{self.year} {self.make} {self.model}, Price: ${self.price}"


class CarDealership:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        """Додає автомобіль до списку доступних для продажу"""
        self.cars.append(car)

    def sell_car(self, car):
        """Продає автомобіль, видаляючи його зі списку"""
        if car in self.cars:
            self.cars.remove(car)
            print(f"Car sold: {car}")
        else:
            print("This car is not available for sale.")

    def __str__(self):
        if not self.cars:
            return "No cars available for sale."
        return "Cars available for sale:\n" + "\n".join(str(car) for car in self.cars)


car1 = Car("Tesla", "Model S", 2022, 79999)
car2 = Car("BMW", "X5", 2021, 60999)
car3 = Car("Audi", "A4", 2020, 35999)

dealership = CarDealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)

print(dealership)

dealership.sell_car(car2)

print(dealership)
