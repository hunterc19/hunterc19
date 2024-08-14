### Aggregating DataFrames

"""
Numbers that summarize datasets
mean()
median()
mode()
max()
min()


example: dogs["height_cm"].mean()

The .agg() method

def pct30(column):
    return column.quantile(0.3)

dogs["weight_kg"].agg(pct30)
Yields: 22.59

def pct40(column):
    return column.quantile(0.4)
dogs["weight_kg"].agg(pct30)
Yields: 45.3
    
Summaries on multiples columns

dogs[["weight_kg", "height_cm"]].agg(pct30)
Yields weight_kg 22.6
       height_cm 45.4
       dtype: float

Multiple summaries

def pct40(column):
    return column.quantile(0.4)

dogs["weight_kg"].agg([pct30, pct40])

Cumulative sum

dogs["weight_kg].cumsum()

Rolling sum is .cumsum()

Other cumulative statistics
.cummax()
.cummin()
.cumprod()
"""

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

#SUMMARY STATISTICS

# Print the head of the sales DataFrame
print("\nHead:\n")
print(sales.head())

# Print the info about the sales DataFrame
print("\nInfo:\n")
print(sales.info())

#MEAN AND MEDIAN

# Print the mean of weekly_sales
print("\nMean:\n")
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print("\nMedian:\n")
print(sales["weekly_sales"].median())

#SUMMARIZING DATES

# Print the maximum of the date column
print("\nMax Date:\n")
print(sales["date"].max())

# EFFICIENT SUMMARIES

# Print the minimum of the date column
print("\nMin Date:\n")
print(sales["date"].min())

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))

#Need up import numpy for the median method
import numpy as np
# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

#CUMULATIVE STATISTICS

#Create filtered sales
sales_1_1 = sales[(sales["department"] == 1) & (sales["store"] == 1)]

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date")

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

###Counting

"""
vet_visits.drop_duplicates(subset=["name"])
dedupe on name

unique_dogs = vet_visits.drop_duplicates(subset=["name","breed"])

unique_dogs["breed"].value_counts(sort=True)

#Gets % of total
unique_dogs["breed"].value_counts(normalize=True)

"""

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store","type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store","department"])
print(store_depts.head())
# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"] == True].drop_duplicates(subset="date")

# Print date col of holiday_dates
print(holiday_dates['date'])

#Couting categorical variables

"""
Avoid double counting:
Cant just count each breed
Remove duplicate names with vet_visits.drop_duplicates(subset="name")
    Gets unique names
Remove duplicate names with vet_visits.drop_duplicates(subset=["name","breed"])
    Gets unique names and breeds
To count the unique dogs:
    unique_dogs["breed"].value_counts()
We can sort it by breed totals too:
    unique_dogs["breed"].value_counts(sort=True)
We can get proportions as well using normalize:
    unique_dogs["breed"].value_counts(normalize=True)
"""
# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

# Grouped Summary Statistics
"""
dogs.groupby("color")["weight_kg"].mean()
dogs.groupby("color")["weight_kg"].agg([min, max, sum])
dogs.groupby(["color", "breed"])["weight_kg"].mean()
dogs.groupby(["color", "breed"])[["weight_kg","height_cm"]].mean()
"""

""" The following example is without using groupby() to show the inefficiency"""
# # Calc total weekly sales
sales_all = sales["weekly_sales"].agg(sum)

# # Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].agg(sum)

# # Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].agg(sum)

# # Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].agg(sum)

# # Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

""" Now to get the same result using groupby() see how much more efficient it is. 
    No longer introducting potential for copy paste errors and is scalable for additional values
"""
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].agg(sum)

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# From previous step, note we can do sum() instead of agg(sum)
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type","is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

## Multiple Grouped Summaries with Numpy
sales_stats = sales.groupby("type")["weekly_sales"].agg([min, max, sum])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment","fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])


# Print unemp_fuel_stats
print(unemp_fuel_stats)

# Pivot Tables
"""
dogs.groupby("color")["weight_kg"].mean()
dogs.pivot_table(values="weight_kg", index="color") ## This gives us the mean
dogs.pivot_table(values="wight_kg", index="color", aggfunc=np.median)
Multiple statistics
    dogs.pivot_table(values="weight_kg", index="color", aggfunc=[np.mean, np.median])
Pivot on two variables
    dogs.pivot_table(values="weight_kg", index="color", columns="breed")
Fill missing values
    dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value = 0)
Summing with pivot tables. Does not incorporate the 0s. Summary statistic
    dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value = 0, margins=True)
"""
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday. Note that the default aggregation is mean or average and we do not need to use aggfunc
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="type", columns="department", fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))
# Note that the All column provides an overall mean and not (A+B)/2 because that would be a "mean of means"
