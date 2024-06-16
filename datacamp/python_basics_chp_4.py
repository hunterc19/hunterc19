### CHAPTER 4

## NEXT FEATURE IS TO DO OPERATIONS OVER COLLECTIONS WITH SPEED

"""
NUMPY NUMERIC PYTHON
ALTERNATIVE TO PYTHON LIST: NUMPY ARRAYS
EASY AND FAST - NEED TO INSTALL IN THE COMMAND LINE
pip3 install numpy
import numpy as np
"""

import numpy as np

"""
NumPy remarks
NumPy arrays: contain only one type
all floats, all booleans for example

NumPy Subsetting
bmi[1]
bmi > 23
result is boolean True or False

bmi[bmi > 23]
NumPy array with values that meet criteria
"""

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# Create a numpy array from height_in: np_height_in
#np_height_in = np.array(height_in)

# Print out np_height_in
#print(np_height_in)

# Convert np_height_in to m: np_height_m
#np_height_m = np_height_in * 0.0254

# Print np_height_m
#print(np_height_m)

# Create array from height_in with metric units: np_height_m
#np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
#np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
#bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
#print(bmi)

# Calculate the BMI: bmi
#np_height_m = np.array(height_in) * 0.0254
#np_weight_kg = np.array(weight_lb) * 0.453592
#bmi = np_weight_kg / np_height_m ** 2

# Create the light array
#light = bmi < 21

# Print out light
#print(light)

# Print out BMIs of all baseball players whose BMI is below 21
#print(bmi[light])

# Store weight and height lists as numpy arrays
#np_weight_lb = np.array(weight_lb)
#np_height_in = np.array(height_in)

# Print out the weight at index 50
#print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
#print(np_height_in[100:111])

"""
2D NumPy Arrays

type(array)
numpy.ndarray
N dimensional arrays

np_2d.shape gives us rows and columns

np_2d[:, 1:3] # Returns all rows and 2nd and 3rd columns

np_2d[1, :] # Returns 2nd row and all columns

"""

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# Print out height of 124th player
print(np_baseball[123][0])

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)

"""
NumPy: Basic Statistics

NumPy is good a aggregating data

np.mean
np.median
np.correcoef are height and weight correlated
np.std standard deviations

numpy requires single data type so creates for fast results
"""

# Create np_height_in from np_baseball
np_height_in = np.array(np_baseball[:,0]) # This removes the second column, weight, and only gets the height

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

# Print the correlation 0-1
print(corr[0, 1])

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)
#np_players = np_positions + np_players

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))














