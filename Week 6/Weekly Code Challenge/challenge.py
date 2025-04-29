# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: NumPy array and mean
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Array from 1 to 10
mean_value = np.mean(numbers)  # Calculate mean
print("Task 1: NumPy Array and Mean")
print("Array:", numbers)
print("Mean:", mean_value)
print()

# Task 2: Pandas DataFrame and summary statistics
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 90, 78]}  # Small dataset
df = pd.DataFrame(data)  # Create DataFrame
print("Task 2: Pandas DataFrame Summary")
print(df.describe())  # Show summary statistics
print()

# Task 3: Fetch data from public API
url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=your_api_key"
response = requests.get(url)  # Make API request
if response.status_code == 200:
    weather_data = response.json()
    temp = weather_data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
    print("Task 3: API Weather Data")
    print("London Temperature:", round(temp, 1), "°C")
else:
    print("API request failed")
print()

# Task 4: Matplotlib line graph
days = [1, 2, 3, 4, 5]  # X-axis: days
sales = [100, 120, 130, 140, 150]  # Y-axis: sales
plt.plot(days, sales, marker='o', color='blue')  # Create line plot
plt.title('Sales Over Days')
plt.xlabel('Day')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.savefig('line_graph.png')  # Save graph
plt.show();