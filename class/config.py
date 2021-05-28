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
        return f"Car Name {self.name}\nBrand {self.brand}"


if __name__ == "__main":
    car = Configuration()
