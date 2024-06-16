"""
INTRODUCTING DATAFRAMES
 - Data Manipulation skill track
 - Data Visualization skill track

 
TABLE OF CONTENTS
Chp 1: DataFrames
  - Sorting and subsetting
  - Creating new columns
Chp 2: Aggregating Data
  - Summary Statistics
  - Counting
  - Grouped summary statistics
Chp 3: Slicing and Indexing Data
  - Subsetting using slicing
  - Indexes and subsetting using indexes
Chp 4: Creating and Visualizing Data
  - Plotting
  - Handling missing data
  - Reading data into a DataFrame

pandas is built on NumPy and Matplotlib
NumPy: multidimensional array objects for easy data manipulation that Pandas uses to store data
Matplotlib: powerful data visualization capabilities

Rectangular data > columns and rows
Rectangular data in pandas are saved in DataFrames
Different columns can have different data types

dogs.head()
returns first few rows of the data frame
this is a good way to query large dataframes without querying the entire dataset

dogs.info()
names of columns and datatypes and if has missing values

dogs.shape
rows then columns
attribute and not method, no () at end

dogs.describe()
summary statistics for numerical data
count, mean, median, std, max, etc

dogs.values
yields 2d numpy array

dogs.columns
get all labels for columns

dogs.index
row names
these are index objects 
allows for flexibility in labels (eg. can use row names or row numbers)

The Zen of Python by Tim Peters, Item 13
Pandas does not follow this philosophy
Pandas is a swiss-army knife, allowing you to choose best way to solve

Course covers the most important and relevant ways of doing things
"""
##Exercise 1: 

import pandas as pd
['region', 'state', 'individuals', 'family_members', 'state_pop']


# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness, Shape is not a method so do not need () at the end
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

## Exercise 2:

# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

"""
Sorting and subsetting

dogs.sort_values("column_name", ascending=False)
dogs.sort_values(["column_name_1", "column_name_2"], ascending = [True,False])

dogs["name"]
just return a specific column

dogs[["breed","height_cm]]
outer brackets subset dataframe
inner brackets creating list of column names to subset

dogs["height_cm"] > 50 
# Dogs whose height is more than 50 cm
yields true or false if the row meets the criteria

dogs[dogs["height_cm"] > 50]
yields all row information that meet criteria

dogs[dogs["breed"] == "Labrador"]
yields all row information for labradors

Subsetting based on dates
dogs[dogs["date_of_birth"] < "2015-01-01"]
yields all row information that meets date requirement
Dates are in quotes and written "YYYY-MM-DD"

is_lab = dogs["breed"] == "Labrador"
is_brown = dogs["color"] == "Brown"
# In one line
dogs[(dogs["breed] = "Labrador") & (dogs["color"] == "Brown")]
dogs[is_lab & is_brown]
# This filters dogs df using both filters

subsetting using .isin()

is_black_or_brown = dogs["color"].isin(["Black", "Brown"])
dogs[is_black_or_brown]

"""

## Exercise 3:

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Print the top few rows
print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending = [True,False])

# Print the top few rows
print(homelessness_reg_fam.head())

# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())

## Exercise 4:

# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

# Print the head of the result
print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"]> 10000]

# See the result
print(ind_gt_10k)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)

## Exercise 5:

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[homelessness["region"].isin(["South Atlantic", "Mid-Atlantic"])]

# See the result
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)

"""
NEW COLUMNS

Mutating, transforming, feature engineering
dogs["height_m"] = dogs["height_cm] / 100

Doggy Mass Index

dogs["bmi"] = dogs["weight_kg"] / dogs["height_m"] ** 2
print(dogs.head())

#Example of getting Tall and Skinny Dogs
bmi_lt_100 = dogs[dogs["bmi"] < 100]
bmi_lt_100_height = bmi_lt_100.sort_values("height_cm", ascending=False)
bmi_lt_100_height[["name", "height_cm", "bmi"]]

"""

## Exercise 6:

# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of total that are individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"] 

# See the result
print(homelessness)

# Create indiv_per_10k col as homeless individuals per 10k state pop

homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)
