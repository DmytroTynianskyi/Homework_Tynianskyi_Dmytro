class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def info(self):
        print(f"Транспортний засіб: {
              self.name}, Швидкість: {self.speed} км/год")


class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type

    def info(self):
        super().info()
        print(f"Тип палива: {self.fuel_type}")


class Bicycle(Vehicle):
    def __init__(self, name, speed, type_of_bike):
        super().__init__(name, speed)
        self.type_of_bike = type_of_bike

    def info(self):
        super().info()
        print(f"Тип велосипеда: {self.type_of_bike}")


car = Car("Audi", 180, "Бензин")
bicycle = Bicycle("Trek", 25, "Гірський")

car.info()
bicycle.info()
