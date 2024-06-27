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