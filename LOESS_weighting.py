import pandas as pd
import statsmodels.api as sm

# Step 1: Load the data from CSV file
file_path = 'STAR-1042353-N-Aligned.sortedByCoord_GC_frequency_results.csv'
df = pd.read_csv(file_path)

# Step 2: Fit LOESS
lowess = sm.nonparametric.lowess(df['frequency'], df['GC_content'], frac=0.5)

# Convert the lowess result into a DataFrame for easier handling
lowess_df = pd.DataFrame(lowess, columns=['GC_content', 'predicted_freq'])

# Step 3: Ensure all predicted values are positive
lowess_df['predicted_freq'] = lowess_df['predicted_freq'].apply(lambda x: max(x, 0))

# Step 4: Merge the predictions back to the original DataFrame
merged_df = pd.merge(df, lowess_df, on='GC_content', how='left')

# Step 5: Save the new DataFrame with predictions to a new CSV file
output_file_path = 'STAR-1042353-N-Aligned_with_LOESS_all_Predictions.csv'
merged_df.to_csv(output_file_path, index=False)

# Optionally, print the new DataFrame with predictions to verify
print(merged_df)
