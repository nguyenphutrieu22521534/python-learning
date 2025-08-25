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

#Change a Range of Item Values
fruits[1:3] = ["kiwi", "mango"]
print("After changing a range of items:", fruits)

# With list comprehension you can do all that with only one line of code
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Copy a List
mylist1 = fruits.copy()
print("Copied list:", mylist1)
mylist2 = list(fruits)
print("Copied list using list():", mylist2)
mylist3 = fruits[:]
print("Copied list using slicing:", mylist3)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print("Joined list using +:", list3)
list1.extend(list2)
print("Joined list using extend():", list1)
for x in list2:
    list1.append(x)
print("Joined list using append() in a loop:", list1)

