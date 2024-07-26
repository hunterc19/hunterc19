### CHAPTER 3

## Functions and Packages

"""
Function examples:
type(), max(), min(), round()
reusable code to solve particular task

round(1.68, 1)
1.7

help() # Can explain how functions work

How to find functions: Datacamp, Google
"""

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

help(pow) #tells us how to use the pow function

# Multiple arguements
# combining two lists and sorting the result

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

## Methods

"""
Built-In Functions
max(), len()

Get index of list
Reverse a list

Strings Floats and lists are all objects (object oriented)

Methods: Functions that belong to objects
Methods are called with period after the object

Str: capitalize(), replace(), index()
float: bit_length(), conjugate()
list: index(), count()

List.method
fam.index("mom")

sister.capitalize("lisa")
sister.replace

fam.append("me")
"""
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

## Packages
"""
Packages
- Directory of Python Scripts
- Each script = module
- Specify functions, methods, types
- Thousands available:
  - NumPy - Data Science
  - Matplotlib - Data Viz
  - scikit-learn - ML

Install package
Tell python to download the package

When you import packages you can alias the package name like this
import numpy as np

#import numpy as np

# Import the math package
import math

# Definition of radius
r = 0.43

# Calculate C
##C = 2 * math.pi * r

# Calculate A
#A = math.pi * r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Import radians function of math package
#from math import radians

# Definition of radius
r = 192500

# Travel distance of Moon over 12 degrees. Store in dist.
#dist = r * radians(12)
# phi = angle in radians = 12
# Print out dist
print(dist)


Suppose you want to use the function inv(), 
which is in the linalg subpackage of the scipy package. 
You want to be able to use this function as follows:

my_inv([[1,2], [3,4]])


from scipy.linalg import inv as my_inv


"""