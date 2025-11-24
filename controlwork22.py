class Animal:
    def init(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def init(self, name):
        super().init(name)

    def speak(self):
        return "Woof"


class Cat(Animal):
    def init(self, name):
        super().init(name)

    def speak(self):
        return "Meow"


dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())
print(cat.name, cat.speak())  