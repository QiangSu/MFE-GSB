import pandas as pd

# Load your data from the CSV file
file_path = 'ENST00000229239_output_binned_GC_content.csv'
# The data is expected to be properly spaced or separated by commas, modify read_csv accordingly
df = pd.read_csv(file_path)

# Create a new column for the weighted values, initially set to zero
df['weighted_value'] = 0

# Iterate over each row to calculate weighted values
for index, row in df.iterrows():
    # Finding all matches where Binned_GC_GAPDH equals Binned_GC_Content of the current row
    matches = df[df['Binned_GC_GAPDH'] == row['Binned_GC_Content']]
    if not matches.empty:
        total_weighted_value = 0
        # Calculate sum of products of all matching rows
        for _, match in matches.iterrows():
            total_weighted_value += row['Sum_Frequency'] * match['weighting_factor']
        df.at[index, 'weighted_value'] = total_weighted_value

# Print the DataFrame to verify the results
print(df)

# Save the DataFrame to a new CSV file
output_path = 'updated_ENST00000229239_output_binned_gc_content.csv'
df.to_csv(output_path, index=False)
