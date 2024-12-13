import pandas as pd

# Define the data as a dictionary
sales1 = {
    'store': [1, 2, 1, 2, 1],
    'type': ['A', 'B', 'A', 'B', 'A'],
    'department': [1, 1, 2, 2, 3],
    'date': ['2023-01-01', '2023-01-01', '2023-01-08', '2023-01-08', '2023-01-15'],
    'weekly_sales': [20000.0, 15000.0, 25000.0, 12000.0, 30000.0],
    'is_holiday': [False, False, True, False, True],
    'temperature_c': [22.5, 21.0, 23.0, 19.0, 20.5],
    'fuel_price_usd_per_l': [0.75, 0.80, 0.78, 0.82, 0.77],
    'unemployment': [7.5, 8.0, 7.8, 8.1, 7.7]
}

# Create the DataFrame from the dictionary
sales = pd.DataFrame(sales1)

# Define the data as a dictionary
dogs1 = {
    'name': ['Bella', 'Charlie', 'Lucy', 'Cooper', 'Max','Stella', 'Bernie'],
    'breed': ['Labrador', 'Poodle', 'Chow Chow', 'Schnauzer', 'Labrador','Chihuahua', 'St. Bernard'],
    'color': ['Brown', 'Black', 'Brown', 'Gray', 'Black','Tan', 'White'],
    'height_cm': [56,43,46,49,59,18,77],
    'Weight_kg': [25,23,22,17,29,2,74]
}

# Create the DataFrame from the dictionary
dogs = pd.DataFrame(dogs1)

# Explicit indexes

"""
dogs_ind = dogs.set_index("name")
#You know you've done it correctly if the index is left aligned
dogs_ind.reset_index()
#dropping an index. Deletes the index which was name
    dogs_ind.reset_index(drop=True)
#Purpose: Makes subsetting simpler
#    Without indexing
        dogs[dogs["name"].isin(["Bella", "Stella"])]
#    With indexing
        dogs_ind = dogs.set_index("name")
        dogs_ind.loc[["Bella", "Stella]]
#Index Values do not need to be unique
#    If we have multiple dogs with the same breed
#    they will both show up as their own line item if we index by breed
dogs_ind2 = dogs.set_index("breed")
dogs_ind2.loc["Labrador"]
# Multi level indexes aka hierarchical indexes
dogs_ind3 = dogs.set_index(["breed","color"])
# Inner level of index  color is nested inside of outer level breed
# Subset outer level (breed) with a list
dogs_ind3.loc[["Labrador","Chihuahua"]]
# Subset the inner level with a list of tuples
dogs_ind3.loc[[("Labrador","Brown"),("Chihuahua","Tan")]]
# Sorting by index values. Outer to inner by default in ascending order
dogs_ind3.sort_index()
# Contraolling sort_index
dogs_ind3.sort_index(level=["color","breed"], ascending=[True,False])

# Index values are just data
# Indexes violate "tidy data" principles
    Index values do not get their own column
"""

temperatures1 = {
    'date': ['2023-01-01', '2023-01-01', '2023-01-08', '2023-01-08', '2023-01-15'],
    'city': ['Abidjan', 'Abidjan', 'Abidjan', 'Abidjan', 'Abidjan'],
    'country': ['Cote Dlvoire', 'Cote Dlvoire','Cote Dlvoire','Cote Dlvoire','Cote Dlvoire'],
    'avg_temp_c': [27.293, 27.685, 29.061, 28.162, 27.547]
}

# Create the DataFrame from the dictionary
temperatures = pd.DataFrame(temperatures1)

# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil",'Rio De Janeiro'), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True,False]))

# Slicing and subsetting with .loc and .iloc

breeds = ['Labrador',
          'Poodle',
          'Chow Chow',
          'Schnauzer',
          'Labrador',
          'Chihuahua',
          'St. Bernard']


"""
Slicing the above list, does not include the final value
breeds[2:5]
Beginning of list
breeds[:3] #First 3 items
Slice entire list
    breeds[:]

Sort the index before you slice
dogs_srt = dogs.set_index(["breed", "color"]).sort_index()

Slicing the outer index level
    dogs_srt.loc["Chow Chow":"Poodle"]
2 major differences compared to slicing lists
    1. specify index values instead of row numbers
    2. final value is included in slicing index

Slicing the inner index levels badly
dogs_srt.loc["Tan":"Grey"]
This will give use a blank dataframe

Slicing the innner index levels correctly
dogs_srt.loc[
        ("Laborador", "Brown"):("Schnauzer","Grey")]

Slicing columns
dogs_srt.loc[:, "name":"height_cm"]
colon here is the first arguement to not filter out any rows

Slice rows and columns together:
dogs_srt.loc[
    ("Laborador", "Brown"):("Schnauzer","Grey"),
    "name":"height_cm"]

Use case for slicing (sorting by dates)
dogs = dogs.set_index("date_of_birth").sort_index()
dogs.loc["2014-08-25":"2016-09-16"]
slicing by partial dates
dogs.loc["2014":"2016"]
subsetting by row/column number, final values not included 
dogs.iloc[2:5, 1:4]
"""
# Slicing Index Values 
'''
first:last syntax
can be sliced by index values or row/column number
index values method uses .loc[] method
can only slice an index if the index is sorted using .sort_index()
outer level:  first and last can be strings
inner level: first and last should be tuples
if pass a single slice to .loc[], it will slice the rows

'''
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])

# Slicing in both directions
# Data frames are two-dimensional objects, it is often natural to slice both dimensions at once by passing two agruments to .loc[]

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,"date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"),"date":"avg_temp_c"])

## Slicing Time Series
'''
Slicing is particularly useful for time series since it's a common thing to want to filter 
for data within a date range. Add the date column to the index, then use .loc[] to perform 
the subsetting. The important thing to remember is to keep your dates in ISO 8601 format, 
that is, "yyyy-mm-dd" for year-month-day, "yyyy-mm" for year-month, and "yyyy" for year.
'''
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]

print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc[("2010-08"):("2011-02")])

#Subsetting by row/column number
