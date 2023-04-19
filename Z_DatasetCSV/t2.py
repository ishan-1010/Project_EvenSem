import pandas as pd

# Read the three CSV files into separate dataframes
df1 = pd.read_csv('user_1_data.csv')
df2 = pd.read_csv('user_2_data.csv')
df3 = pd.read_csv('user_3_data.csv')

# Concatenate the dataframes vertically (i.e., stack them on top of each other)
combined_df = pd.concat([df1, df2, df3], axis=0)

# Write the combined dataframe to a new CSV file
combined_df.to_csv('combined_file.csv', index=False)

print("Combined CSV file has been created: combined_file.csv")
