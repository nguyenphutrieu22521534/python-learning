# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)

# Adding elements to a set
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing elements from a set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Performing set operations
another_set = {4, 5, 6, 7, 8}

# Union
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# Intersection
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

# Difference
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)

# Checking membership
print("Is 2 in the set?", 2 in my_set)
print("Is 10 in the set?", 10 in my_set)

# Difference update
my_set.difference_update(another_set)
print("Set after difference update with another_set:", my_set)

# Symmetric Differences
symmetric_diff_set = my_set.symmetric_difference(another_set)
print("Symmetric difference of sets:", symmetric_diff_set)

# Symmetric Difference Update
my_set.symmetric_difference_update(another_set)
print("Set after symmetric difference update with another_set:", my_set)