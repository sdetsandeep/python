# ==========================================
# Python Data Types Example
# ==========================================

# -------------------------------
# 1. Text Type : str
# -------------------------------

name = "Sandeep"

print("String Value :", name)
print("Data Type :", type(name))
print()


# -------------------------------
# 2. Numeric Types
# -------------------------------

# Integer (Whole Number)
age = 42

print("Integer Value :", age)
print("Data Type :", type(age))
print()


# Float (Decimal Number)
percentage = 89.75

print("Float Value :", percentage)
print("Data Type :", type(percentage))
print()


# Complex Number
number = 5 + 3j

print("Complex Value :", number)
print("Data Type :", type(number))
print()


# -------------------------------
# 3. Sequence Types
# -------------------------------

# List (Can be Changed)
fruits = ["Apple", "Banana", "Mango"]

print("List :", fruits)
print("Data Type :", type(fruits))
print()


# Tuple (Cannot be Changed)
colors = ("Red", "Green", "Blue")

print("Tuple :", colors)
print("Data Type :", type(colors))
print()


# Range
numbers = range(1, 6)

print("Range :", list(numbers))
print("Data Type :", type(numbers))
print()


# -------------------------------
# 4. Mapping Type
# -------------------------------

# Dictionary (Key : Value)
student = {
    "Name": "Rahul",
    "Age": 15,
    "Class": 7
}

print("Dictionary :", student)
print("Data Type :", type(student))
print()


# -------------------------------
# 5. Set Types
# -------------------------------

# Set (Unique Values)
languages = {"Python", "Java", "C++"}

print("Set :", languages)
print("Data Type :", type(languages))
print()


# Frozen Set (Cannot be Changed)
fset = frozenset({"Apple", "Banana", "Mango"})

print("Frozen Set :", fset)
print("Data Type :", type(fset))
print()


# -------------------------------
# 6. Boolean Type
# -------------------------------

is_student = True

print("Boolean Value :", is_student)
print("Data Type :", type(is_student))
print()


# -------------------------------
# 7. Binary Types
# -------------------------------

# Bytes
b = bytes([65, 66, 67])

print("Bytes :", b)
print("Data Type :", type(b))
print()


# Bytearray
ba = bytearray([65, 66, 67])

print("Bytearray :", ba)
print("Data Type :", type(ba))
print()


# Memoryview
mv = memoryview(bytes([65, 66, 67]))

print("Memoryview :", mv)
print("Data Type :", type(mv))
print()


# -------------------------------
# 8. None Type
# -------------------------------

value = None

print("None Value :", value)
print("Data Type :", type(value))
print()