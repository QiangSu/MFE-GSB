import math
import pandas as pd  # Importing pandas library

# Read the CSV file, assuming the file is in the same directory as this script
df = pd.read_csv('8NS_rep2.csv')


# Define the given equation as a function
def calculate_y(x):
    pi = math.pi  # Pi constant
    exp = math.exp  # Exponential function
    sqrt = math.sqrt  # Square root function

    # Equation as given in the initial script
    y = 868.34012 + (64642.38276 / (3.7897  * sqrt(pi / 2))) * exp(-2 * ((x - (-6.122)) / 3.7897 ) ** 2)
    return y


# Apply the calculate_y function to the 'MFE_category' column and store the results in a new column 'y'
df['y'] = df['MFE_category'].apply(calculate_y)

# Write the results to a new CSV file
df.to_csv('8NS_rep2_output.csv', index=False)

print('Calculation completed and output.csv generated.')
