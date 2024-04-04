import pandas as pd

# Load the dataset
df = pd.read_csv('MFE_1042353N_GAPDH201.csv')

# If there are duplicates in 'GC_category' with different 'average', this will take the first occurrence.
# Adjust this step according to how you want to handle duplicates.
df_unique = df.drop_duplicates(subset='MFE_category', keep='first')

# Create a mapping of GC_category to average with the unique DataFrame
average_mapping = pd.Series(df_unique.rf_MFE_ave.values, index=df_unique.MFE_category).to_dict()

# Map each 'GC' to its corresponding 'average' using the unique mapping
df['MFE_average'] = df['MFE'].map(average_mapping)

# Create a new column to show the pairing result of GC and its corresponding average value
df['pairing'] = df.apply(lambda row: f"({row['MFE']}, {row['MFE_average']})", axis=1)

# Display the result
print(df[['MFE', 'pairing']])

# Optionally, save this enriched dataset to a new CSV file
df.to_csv('mapped_MFE_1042353N_GAPDH201.csv', index=False)
