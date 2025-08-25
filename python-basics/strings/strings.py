#Get the character at position 1
a = "Hello, World!"
print(a[1])

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# Get the length of a string
print(len(a))

# Check if a certain phrase or character is present in a string
txt = "The best things in life are free!"
print("free" in txt)

# Check if a certain phrase or character is NOT present in a string
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Slicing a string
b = "Hello, World!"
print(b[2:5])

# Modify string case
c = "hello, world!"
print(c.upper())
print(c.lower())

# Remove whitespace from the beginning or the end
d = "   Hello, World!   "
print(d.strip()) # returns "Hello, World!"

# Replace a string with another string
e = "Hello, World!"
print(e.replace("H", "J"))

# Split a string into a list
f = "Hello, World!"
print(f.split(",")) # returns ['Hello', ' World!']

# Format strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))