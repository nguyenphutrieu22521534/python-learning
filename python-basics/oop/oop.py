class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p1 = Person("Alice", 25)   # tạo đối tượng Person tên Alice, 25 tuổi
print(p1.greet())          # gọi phương thức greet

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year
    def welcome(self):
        return f"Welcome {self.name} to the class of {self.year}"

p2 = Student("Mike", "21", 2019)
print(p2.welcome())