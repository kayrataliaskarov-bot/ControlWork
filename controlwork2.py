class Person:
    def init(self):
        self.__age = 0

    def set_age(self, age):
        if age < 0:
            print("Возраст не может быть отрицательным!")
        else:
            self.__age = age

    def get_age(self):
        return self.__age


p = Person()
p.set_age(25)
print(p.get_age())

p.set_age(-5)
print(p.get_age())


