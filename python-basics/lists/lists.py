# lists.py

# Example of list creation
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing elements by index
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Slicing lists
print("First two fruits:", fruits[0:2])

# Adding an element to the list
fruits.append("orange")
print("After appending orange:", fruits)

# Removing an element from the list
fruits.remove("banana")
print("After removing banana:", fruits)

# Sorting the list
fruits.sort()
print("Sorted fruits:", fruits)

# Length of the list
print("Number of fruits:", len(fruits))