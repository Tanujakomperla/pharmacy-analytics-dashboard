import pandas as pd

# Excel file location
file_path = r"C:\Users\Tanuja\Desktop\Pharmacy_Analytics_Dashboard\data\Pharmacy_Student_Performance_Dataset.xlsx"

# Read Excel
df = pd.read_excel(file_path)

print("\n======================================")
print("   PHARMACY STUDENT ANALYTICS")
print("======================================")

# -----------------------------
# 1. BEFORE CLEANING
# -----------------------------

print("\nBEFORE CLEANING")
print("----------------")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())


# -----------------------------
# 2. DATA CLEANING
# -----------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()


# -----------------------------
# 3. AFTER CLEANING
# -----------------------------

print("\nAFTER CLEANING")
print("---------------")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())


# -----------------------------
# 4. FINAL DATASET
# -----------------------------

print("\nFinal Dataset:")
print(df.head())

print("\nData Cleaning Completed Successfully!")