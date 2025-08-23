# dictionaries.py

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

# Adding a new key-value pair
my_dict["job"] = "Engineer"
print("Updated Dictionary:", my_dict)

# Removing a key-value pair
del my_dict["age"]
print("Dictionary after deletion:", my_dict)

# Checking if a key exists
if "city" in my_dict:
    print("City exists in the dictionary.")

# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Common dictionary methods
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)