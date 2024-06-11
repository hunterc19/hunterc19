### CHAPTER 1

## BASIC ARITHMATIC

# Addition
print(4 + 5) #important that there are spaces between the numbers you are running arithmatic on

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)

# Division
print(10 / 2)

## VARIABLES AND TYPES

"""
VARIABLE - SPECIFIC, CASE-SENSITIVE NAME
YOU ARE "DECLARING" THE VARIABLE, AND YOU "CALL" THE VALUE THROUGH A VARIABLE NAME
IMAGEIN 1.79 M AND 68.7 KG FOR HEIGHT AND WEIGHT

height = 1.79
weight = 68.7
bmi = weight / height ** 2 

# THE ** IS AN EXPONENT

PYTHON TYPES

TYPE(VARIABLE)

EX: TYPE(BMI) WILL YIELD FLOAT
OTHER EXAMPLES: FLOAT, INT, STRING, BOOLEAN

STR CAN BE DOUBLE OR SINGLE QUOTES
BOOL can be True or False

Code will behave differently for differnt python types

"""

## VARIABLE ASSIGNMENT

# I created a variable with the value of 5
x = 5

# = in python means assignment, it does not test equality

"""How much money would you have saved four months from now,
 if you saved $10 each month?"""

# Create a variable savings
savings = 100

# Print out savings
print(savings)

# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Add new_savings to your savings
total_savings = new_savings + savings

# Print total_savings
print(total_savings)

"""
DATA TYPES:
float, or floating point: a number that has both an integer and fractional part, separated by a point. 1.1, is an example of a float.
str, or string: a type to represent text. You can use single or double quotes to build a string.
bool, or boolean: a type to represent logical values. It can only be True or False (the capitalization is important!)
"""

# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True

"""
You can use the type() function to find out the type of a value or a variable that refers to that value
"""

type(intro)

"""
Calculate the product of monthly_savings and num_months. Store the result in year_savings.

What do you think the resulting type will be? Find out by printing out the type of year_savings.

Calculate the sum of intro and intro and store the result in a new variable doubleintro.

Print out doubleintro. Did you expect this?
"""

monthly_savings = 10
num_months = 12
intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings and num_months
year_savings = monthly_savings * num_months

# Print the type of year_savings
print(type(year_savings))

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)

"""
TYPE CONVERSION: CONVERTING THE NUMBERS TO STRINGS SO THAT THEY CAN BE INTERPRETTED IN A STRING SUMMARY 
"""

# Definition of savings and total_savings
savings = 100
total_savings = 150

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

"""
YOU CAN DO MULTIPLCATION ON STRINGS LIKE THIS 
("HEY" * 2)
"""
print("HEY" * 2)

### CHAPTER 2

## PYTHON LISTS

"""
PYTHON LISTS: A list is a way to give a single name to a collection of values. 
These values, or elements, can have any type; they can be floats, integer, 
booleans, strings, but also more advanced Python types, even lists. It's 
perfectly possible for a list to contain different types as well.

BRACKETS ARE HOW YOU MAKE A LIST

- Name a collection of values
- Contain any type
- Contain different types
"""

list1 = [1,2,3,4]
print(list1)

list_of_lists = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
print(list_of_lists)

# you can check the data type of the list as well

type(list1)

"""
Example
"""
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall,kit,liv,bed,bath]

# Print areas
print(areas)


areas2 = ["hallway", hall,
         "kitchen", kit,
         "living", liv,
         "bedroom", bed,
         "bathroom", bath]

# Print areas
print(areas2)

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall], #index 0 and 1
         ["kitchen", kit], #index 2 and 3
         ["living room", liv], #index 4 and 5
         ["bedroom", bed], #index 6 and 7
         ["bathroom", bath]] #index 8 and 9

# Print out house
print(house)

# Print out the type of house
print(type(house))

"""
SUBSETTING LISTS
INDEXING STARTS WITH ZERO

LIST SLICING
SELECT MULTIPLE ELEMENTS FROM THE LIST

[start:end]
[inclusive:exclusive]
"""

house[-2] #gives us the second list from the right bedroom

#PRACTICE WITH SUBSETTING

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = (areas[3] + areas[-3])
# The parentheses is super important here. determines if you are making a list or saving the variable as an int

# Print the variable eat_sleep_area
print(eat_sleep_area)

#SLICING AND DICING

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs first 6 elements
downstairs = areas[0:6]

# Use slicing to create upstairs last 4 elements
upstairs = areas[-4:11]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# YOU DONT NEED TO SPECIFIC THAT YOU WANT TO START FROM THE BEGINNING OR STOP AT THE END

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[-4:]

print(downstairs)
print(upstairs)

# SUBSETTING LISTS OF LISTS

house = [["hallway", hall], #index 0 and 1
         ["kitchen", kit], #index 2 and 3
         ["living room", liv], #index 4 and 5
         ["bedroom", bed], #index 6 and 7
         ["bathroom", bath]] #index 8 and 9

house[-1][1]

# LIST MANIPULATION
"""
CHANGE LIST ELEMENTS
ADD OR REMOVE ELEMENTS
"""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

print(areas)

#Adding Elements

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

del(areas[-4:-2])

#EXPLICIT AND REFERENCE-BASED COPIES

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy EXPLICIT TO NOT IMPACT areas list
# THIS IS A REFERENCE: areas_copy = areas
areas_copy = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
