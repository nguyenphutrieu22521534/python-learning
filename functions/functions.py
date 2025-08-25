# Define a function that adds two numbers
def add_numbers(a, b):
    return a + b

# Define a function that prints a greeting
def greet(name):
    print(f"Hello, {name}!")

# Call the functions
result = add_numbers(5, 3)
print("Sum:", result)

greet("Alice")

# arbitrary arguments
def greet_people(*names):
    for name in names:
        print(f"Hello, {name}!")
greet_people("Alice", "Bob", "Charlie")

# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
def greet_person(name="Guest"):
    print(f"Hello, {name}!")
greet_person()  # Uses default value
greet_person("Bob")  # Overrides default value

# Passing a List as an Argument
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)
fruits_list = ["apple", "banana", "cherry"]
print_fruits(fruits_list)

# recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

# lambda function
square = lambda x: x * x
print("Square of 4:", square(4))

# map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared Numbers:", squared_numbers)

# filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# reduce function
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers:", product)

# nested functions
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()
outer_function("Hello from the outer function!")