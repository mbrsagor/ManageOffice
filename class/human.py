class Human(object):
    def __init__(self, name, age, gender, height, weight, is_disabled):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.is_disabled = is_disabled

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nHeight: {self.height}\nWeight: {self.weight}\nDisabled: {self.is_disabled}"


class Men(object):

    @staticmethod
    def boy():
        return Human('Sagor', 26, 'Male', 5.5, "51.30 KG", False)


class Woman(object):

    @staticmethod
    def girl():
        return Human("Isha", 3, "Female", 3.0, "12KG", False)


men = Men()
woman = Woman()

print(men.boy())
print("\n")
print(woman.girl())
