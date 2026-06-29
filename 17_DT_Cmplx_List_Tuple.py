#complax number
cmp = 5+3j;

print("Complex Value :", cmp)
print("Data Type :", type(cmp))
print()

# LIST  / SEQUENcE

# List (Can be Changed)
fruits=["Apple", "Mango", "Banana", "Kela", "SEB", "Aam"]
print( "The list of fruit is ", fruits)
print("The type of fruit is =", type(fruits))

# Tuple (Cannot be Changed)
colors = ("Red", "Green", "Blue")

print("Tuple :", colors)
print("Data Type :", type(colors))
print()

# line of code to explain the List can be changed
fruits[1] = "Orange"
print("After changing  the item at 1st index new List is ")
print( "The list of fruit is ", fruits)

colors(1)="blue";  # Error   colors(1)="blue"; SyntaxError: cannot assign to function call here
print("After changing  the item at 1st index new color is ")
print( "The list of fruit is ", colors)
