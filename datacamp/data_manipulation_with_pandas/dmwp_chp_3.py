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

