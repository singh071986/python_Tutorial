import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('gpa.csv')

# Step 2: View the DataFrame
# In interactive environments (like Jupyter), you can just write 'df' to display it.
# In scripts, use print(df) to show the DataFrame in the console.
print('Full DataFrame:')
print(df)

# Step 3: View the top rows
print('\nTop rows using head():')
print(df.head())

# Step 4: Extract columns
inputs = df[['HighSchool_GPA']]
target = df['University_GPA']
print('\nInputs (HighSchool_GPA):')
print(inputs)
print('\nTarget (University_GPA):')
print(target)

# Step 5: Extract rows using .loc and .iloc
print('\nRows 2 to 4 using .loc:')
print(df.loc[1:3])
print('\nRows 2 to 4 using .iloc:')
print(df.iloc[1:4])

# If you are using Jupyter Notebook, you can display the DataFrame by just writing:
# df
