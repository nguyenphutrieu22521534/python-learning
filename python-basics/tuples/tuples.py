# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Accessing elements in a tuple
first_element = my_tuple[0]
print("First element:", first_element)

# Negative indexing
last_element = my_tuple[-1]
print("Last element:", last_element)

# Slicing a tuple
sliced_tuple = my_tuple[1:4]
print("Sliced tuple (index 1 to 3):", sliced_tuple)

# Tuples are immutable
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)

# Creating a tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# Nested tuples
nested_tuple = (my_tuple, mixed_tuple)
print("Nested tuple:", nested_tuple)

# Update Tuple

# Unpacking a tuple
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# Using asterisk (*) to unpack
first, *middle, last = my_tuple
print("First:", first)
print("Middle:", middle)
print("Last:", last)

