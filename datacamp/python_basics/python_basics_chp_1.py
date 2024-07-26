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