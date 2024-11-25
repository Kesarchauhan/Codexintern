import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\Kesar\Desktop\Sales_Data.csv"  
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few Rows of the Dataset:")
print(data.head())

# Display basic information about the dataset
print("\nDataset Info:")
print(data.info())

# Display summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Calculate the average (mean) of a column (e.g., 'Sales')
avg = data['Sales'].mean()
print(f"\nAge avarage: {avg}")

# Find the median of a column (e.g., 'Profit')
Median = data['Profit'].median()
print(f"\nMedian Profit: {Median}")

# Count unique values in a categorical column (e.g., 'Category')
Uv = data['Category'].value_counts()
print("\nUnique Categories and Their Counts: {Uv}")

# Filter data where Sales > 500
high_sales = data[data['Sales'] > 500]
print("\nRows with Sales > 500:")
print(high_sales)

Lowest_sales = data[data['Sales'] < 500]
print("\nRows with Sales < 500:")
print(Lowest_sales)
# Data visualisation
plt.figure(figsize=(10, 6))
plt.bar(data['Product'], data['Sales'], color='green')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()


