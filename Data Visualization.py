import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd




# Load Mobile Device Usage dataset
file_path = r"C:\Users\Kesar\Desktop\Sales_Data.csv"  
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 Rows of the Dataset:")
print(data.head())

# Dataset summary
print("\nDataset Summary:")
print(data.info())

# Check for missing values
print("\nMissing Values Count:")
print(data.isnull().sum())

# Check columns in the dataset to confirm their names
print("\nColumns in the Dataset:")
print(data.columns)


# Pie Chart for Category Distribution
category_sales = data.groupby('Category')['Sales'].sum()
plt.figure(figsize=(8, 8))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99', '#ffcc99'])
plt.title('Sales Distribution by Category')
plt.show()

# Histogram for Sales Frequency
plt.figure(figsize=(10, 6))
plt.hist(data['Sales'], bins=10, color='skyblue', edgecolor='black')
plt.title('Sales Frequency Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# Bar Chart for Sales by Product
plt.figure(figsize=(10, 6))
plt.bar(data['Product'], data['Sales'], color='orange')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()

# Heatmap for Correlation between Variables
correlation_matrix = data[['Sales', 'Profit', 'Discount', 'Quantity']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Boxplot for Sales Distribution
plt.figure(figsize=(8, 6))
sns.boxplot(x=data['Sales'])
plt.title('Sales Distribution')
plt.show()
