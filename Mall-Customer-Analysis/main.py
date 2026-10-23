
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# 2. Understand the dataset
print("First 5 rows:")
print(df.head())

print("\nDataset size:", df.shape)
print("\nDataset information:")
df.info()

# 3. Check data quality
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# 4. Analyze the data
print("\nBasic statistics:")
print(df.describe())

print("\nCustomers by gender:")
print(df["Genre"].value_counts())

print("\nAverage spending score by gender:")
print(df.groupby("Genre")["Spending Score (1-100)"].mean())

# 5. Graph 1: Customer count by gender
df["Genre"].value_counts().plot(kind="bar")
plt.title("Customers by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("graph1.png")
plt.show()

# 6. Graph 2: Age distribution
plt.hist(df["Age"], bins=10, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("graph2.png")
plt.show()

# 7. Graph 3: Income vs spending score
plt.scatter(df["Annual Income (k$)"], df["Spending Score (1-100)"])
plt.title("Income vs Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.tight_layout()
plt.savefig("graph3.png")
plt.show()

print("\nAnalysis completed!")
