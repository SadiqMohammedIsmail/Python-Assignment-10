# assignment.py
import numpy as np
import pandas as pd

# ==========================================
# PART 1: NumPy Array Operations
# ==========================================
print("--- NumPy Array Operations ---\n")

# 1. Create a 1D NumPy Array
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])
print("1. Week 1 Temperatures Array:", temperatures_w1)

# 2. Inspection and Properties
print("\n2. Array Properties:")
print(f"   Shape: {temperatures_w1.shape}")
print(f"   Data Type: {temperatures_w1.dtype}")
print(f"   Number of elements: {temperatures_w1.size}")

# 3. Array Operations
temperatures_w1_f = (temperatures_w1 * 9/5) + 32
print("\n3. Array Operations:")
print("   Converted to Fahrenheit:", temperatures_w1_f)
print(f"   Maximum Temperature: {temperatures_w1.max()} °C")
print(f"   Minimum Temperature: {temperatures_w1.min()} °C")
print(f"   Mean Temperature: {temperatures_w1.mean():.2f} °C")

# 4. Array Slicing and Indexing
print("\n4. Slicing 1D Array:")
print("   First three days:", temperatures_w1[:3])
print("   Weekend (last two days):", temperatures_w1[-2:])
print("   Middle three days:", temperatures_w1[2:5])

# 5. Create a 2D Array
temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],  # Week 1
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]   # Week 2
])

# 6. Inspect and Slice the 2D Array
print("\n6. 2D Array Properties & Slicing:")
print(f"   Shape: {temperatures.shape}")
print(f"   Data Type: {temperatures.dtype}")
print(f"   Total elements: {temperatures.size}")
print("   Week 1 temperatures:", temperatures[0, :])
print("   Week 2 temperatures:", temperatures[1, :])
print("   Weekends (last two days) for both weeks:\n", temperatures[:, -2:])


# ==========================================
# PART 2: Pandas Series
# ==========================================
print("\n\n--- Pandas Series ---\n")

# 1. Creating Pandas Series
marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'],
    name='marks'
)
print("1. Initial Marks Series:\n", marks, sep="")

# 2. Indexing and Slicing
print("\n2. Indexing and Slicing Series:")
print("   Mark of 1st rank student (integer index 0):", marks.iloc[0])
print("   Top 3 ranks using .loc:\n", marks.loc['Rank1':'Rank3'], sep="")
print("   Mark of 3rd rank student using .iloc:", marks.iloc[2])
print("   Ranks where marks > 90:\n", marks[marks > 90], sep="")

# 3. Manipulating Series
print("\n3. Manipulating Series:")
marks.loc['Rank1'] = 100
print("   Modified Rank 1 to 100:\n", marks, sep="")

marks = marks.drop('Rank5')
print("   Removed last rank (Rank5):\n", marks, sep="")

cgpa = marks / 10
print("   Computed CGPA (Marks / 10):\n", cgpa, sep="")


# ==========================================
# PART 3: Pandas DataFrame
# ==========================================
print("\n\n--- Pandas DataFrame ---\n")

# 1. Creating Pandas DataFrame
data = {
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Furniture', 'Electronics'],
    'Region': ['North', 'South', 'North', 'East', 'West', 'North', 'East', 'West', 'South', 'North'],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
}
transactions = pd.DataFrame(data)

# 2. Data Exploration
print("2. Data Exploration:")
print("\n--- DataFrame Head ---")
print(transactions.head())
print("\n--- DataFrame Tail ---")
print(transactions.tail())
print(f"\n   Shape: {transactions.shape}")
print(f"   Column Names: {list(transactions.columns)}")
print("\n--- Data Types ---")
print(transactions.dtypes)

print("\n--- Selecting ProductCategory and Amount ---")
print(transactions[['ProductCategory', 'Amount']])

print("\n--- Last 3 Columns using iloc ---")
print(transactions.iloc[:, -3:])

print("\n--- Filtered: Region is 'North' and Amount > 200 ---")
print(transactions[(transactions['Region'] == 'North') & (transactions['Amount'] > 200)])

print("\n--- Value Counts for ProductCategory ---")
print(transactions['ProductCategory'].value_counts())

print("\n--- Unique Values in Region ---")
print(transactions['Region'].unique())

print("\n--- Mean Amount Grouped by Region ---")
print(transactions.groupby('Region')['Amount'].mean())

# 3. Manipulating the DataFrame
print("\n3. Manipulating the DataFrame:")

# Modify Amount for TransactionID 102 to 165
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165
print("\n--- Modified Transaction 102 Amount to 165 ---")
print(transactions.head(2))

# Add 'Discount' column (10% of Amount)
transactions['Discount'] = transactions['Amount'] * 0.10
print("\n--- Added 'Discount' Column ---")
print(transactions.head(2))

# Remove the row with TransactionID 109
transactions = transactions[transactions['TransactionID'] != 109]
print("\n--- Removed Row with TransactionID 109 ---")
print(transactions)

# Delete the 'Discount' column
transactions = transactions.drop(columns=['Discount'])
print("\n--- Deleted 'Discount' Column ---")
print(transactions.head(2))
