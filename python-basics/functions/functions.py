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