# overriding methods trong Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def move(self):
        return f"{self.name} is moving"


class Dog(Animal):
    def speak(self):  # Override method
        return f"{self.name} says Woof!"

    def move(self):  # Override method
        return f"{self.name} is running"


class Cat(Animal):
    def speak(self):  # Override method
        return f"{self.name} says Meow!"


# Sử dụng
animal = Animal("Generic")
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(animal.speak())  # Generic makes a sound
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!