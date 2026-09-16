import pandas as pd

# Excel file
file_path = r"C:\Users\Tanuja\Desktop\Pharmacy_Analytics_Dashboard\data\Pharmacy_Student_Performance_Dataset.xlsx"

# Read data
df = pd.read_excel(file_path)

# Clean data
df = df.drop_duplicates()
df = df.dropna()

print("\n======================================")
print("      CORRELATION ANALYSIS")
print("======================================")

# --------------------------------
# 1. Attendance vs Final Marks
# --------------------------------

attendance_corr = df["Attendance_%"].corr(df["Final_Marks"])

print("\n1. Attendance vs Final Marks")
print("--------------------------------")
print("Correlation:", round(attendance_corr, 3))


# --------------------------------
# 2. Study Hours vs Final Marks
# --------------------------------

study_corr = df["Study_Hours_Per_Day"].corr(df["Final_Marks"])

print("\n2. Study Hours vs Final Marks")
print("--------------------------------")
print("Correlation:", round(study_corr, 3))


# --------------------------------
# 3. Internal Average vs Final Marks
# --------------------------------

internal_corr = df["Internal_Average"].corr(df["Final_Marks"])

print("\n3. Internal Average vs Final Marks")
print("--------------------------------")
print("Correlation:", round(internal_corr, 3))


# --------------------------------
# 4. Complete Correlation Matrix
# --------------------------------

print("\n4. CORRELATION MATRIX")
print("--------------------------------")

numeric_columns = [
    "Attendance_%",
    "Study_Hours_Per_Day",
    "Pharmacology",
    "Pharmaceutics",
    "Pharmacognosy",
    "Internal_Average",
    "Final_Marks"
]

correlation_matrix = df[numeric_columns].corr()

print(correlation_matrix)


print("\n======================================")
print("      CORRELATION ANALYSIS COMPLETED")
print("======================================")