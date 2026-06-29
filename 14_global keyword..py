def myfunc():
  global x
  x = "fantastic"

myfunc()
print ("====================================================\n")

print("Python is " + x)


print ("====================================================\n")


""" To change the value of a global variable inside a function, refer to the variable by 
 using the global keyword:
"""

y = "Great"

def myfunc():
  global y
  y = "Gzzzzzzb"

myfunc()

print("Python is " + y)
print ("====================================================\n")