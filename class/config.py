class Configuration(object):
    """
        The class basic configuration of the Car
    """

    def __init__(self, name, price, brand, weight, color, cc=55000):
        self.name = name
        self.price = price
        self.brand = brand
        self.weight = weight
        self.color = color
        self.cc = cc

    def __str__(self):
        return f"Car Name: {self.name}\nBrand: {self.brand}"


class Car(object):

    def my_car(self):
        _car = Configuration("BMW", 2000, "New", "50000", "Red", 40404)
        return _car


car = Car()
print(car.my_car())
