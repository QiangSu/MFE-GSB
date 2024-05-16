import pandas as pd

# Load the CSV data into a DataFrame
data = pd.read_csv('hexamer_frequencies.csv')

# Create a dictionary to map Hexamer to weighting_factor
hexamer_to_weight = dict(zip(data['Hexamer'], data['weighting_factor']))

# Function to multiply the weights with the frequency if the hexamers match
def multiply_values(row):
    hexamer = row['ENST00000229239_Hexamer']
    frequency = row['ENST00000229239_Frequency']
    # Get the weighting factor from the dictionary, default to 1 if not found
    weighting_factor = hexamer_to_weight.get(hexamer, 1)
    return frequency * weighting_factor

# Apply the function along the rows
data['weighted_frequency'] = data.apply(multiply_values, axis=1)

# Now the DataFrame includes a new column 'weighted_frequency'
print(data[['ENST00000229239_Hexamer', 'ENST00000229239_Frequency', 'weighted_frequency']])

# Save the updated DataFrame to a new CSV file
data.to_csv('updated_hexamer_frequencies.csv', index=False)
