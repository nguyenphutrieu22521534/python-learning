# Variable declaration and assignment
name = "Alice"  # String variable
age = 30        # Integer variable
height = 5.5    # Float variable
is_student = True  # Boolean variable

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Variable naming conventions
first_name = "John"  # Valid variable name
_last_name = "Doe"    # Valid variable name
# 1st_name = "Invalid"  # Invalid variable name (cannot start with a number)

# Variable scope
def greet():
    greeting = "Hello, " + name  # Accessing a global variable
    print(greeting)

greet()

# Changing a global variable
age = 31  # Updating the global variable
print("Updated Age:", age)