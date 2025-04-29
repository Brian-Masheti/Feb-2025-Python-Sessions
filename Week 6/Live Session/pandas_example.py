import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create a Dataframe
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Accessing DataFrame columns
print('Accessing a single column:\n', df['Name'])  # Access a single column
print('Accessing multiple columns:\n', df[['Name', 'City']])  # Access multiple columns

# Filter ROws
print('Filtering rows where Age > 28:\n', df[df['Age'] > 28])  # Filter rows based on a condition
print('Filtering rows where City is New York:\n', df[df['City'] == 'New York'])  # Filter rows based on a condition