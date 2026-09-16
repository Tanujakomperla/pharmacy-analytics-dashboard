import pandas as pd

# Excel file
file_path = r"C:\Users\Tanuja\Desktop\Pharmacy_Analytics_Dashboard\data\Pharmacy_Student_Performance_Dataset.xlsx"

# Read data
df = pd.read_excel(file_path)

# Clean data
df = df.drop_duplicates()
df = df.dropna()

print("\n======================================")
print("   PHARMACY STUDENT STATISTICAL ANALYSIS")
print("======================================")

# --------------------------------
# 1. BASIC INFORMATION
# --------------------------------

print("\n1. BASIC INFORMATION")
print("--------------------")

print("Total Students:", len(df))

print("Male Students:", (df["Gender"] == "Male").sum())
print("Female Students:", (df["Gender"] == "Female").sum())


# --------------------------------
# 2. AVERAGE PERFORMANCE
# --------------------------------

print("\n2. AVERAGE PERFORMANCE")
print("----------------------")

print("Average Attendance:",
      round(df["Attendance_%"].mean(), 2), "%")

print("Average Study Hours:",
      round(df["Study_Hours_Per_Day"].mean(), 2))

print("Average Pharmacology:",
      round(df["Pharmacology"].mean(), 2))

print("Average Pharmaceutics:",
      round(df["Pharmaceutics"].mean(), 2))

print("Average Pharmacognosy:",
      round(df["Pharmacognosy"].mean(), 2))

print("Average Final Marks:",
      round(df["Final_Marks"].mean(), 2))


# --------------------------------
# 3. MEDIAN
# --------------------------------

print("\n3. MEDIAN")
print("---------")

print("Median Final Marks:",
      df["Final_Marks"].median())

print("Median Attendance:",
      df["Attendance_%"].median())


# --------------------------------
# 4. STANDARD DEVIATION
# --------------------------------

print("\n4. STANDARD DEVIATION")
print("---------------------")

print("Final Marks SD:",
      round(df["Final_Marks"].std(), 2))

print("Attendance SD:",
      round(df["Attendance_%"].std(), 2))


# --------------------------------
# 5. HIGHEST AND LOWEST
# --------------------------------

print("\n5. HIGHEST AND LOWEST")
print("---------------------")

print("Highest Final Marks:",
      df["Final_Marks"].max())

print("Lowest Final Marks:",
      df["Final_Marks"].min())


# --------------------------------
# 6. PASS ANALYSIS
# --------------------------------

print("\n6. PASS ANALYSIS")
print("----------------")

pass_count = (df["Status"] == "Pass").sum()
total_students = len(df)

pass_percentage = (pass_count / total_students) * 100

print("Passed Students:", pass_count)

print("Pass Percentage:",
      round(pass_percentage, 2), "%")


# --------------------------------
# 7. SUBJECT COMPARISON
# --------------------------------

print("\n7. SUBJECT COMPARISON")
print("---------------------")

subject_averages = {
    "Pharmacology": df["Pharmacology"].mean(),
    "Pharmaceutics": df["Pharmaceutics"].mean(),
    "Pharmacognosy": df["Pharmacognosy"].mean()
}

for subject, average in subject_averages.items():
    print(subject, ":", round(average, 2))


# --------------------------------
# 8. TOP STUDENT
# --------------------------------

print("\n8. TOP PERFORMER")
print("----------------")

top_student = df.loc[df["Final_Marks"].idxmax()]

print("Student ID:", top_student["Student_ID"])
print("Final Marks:", top_student["Final_Marks"])


print("\n======================================")
print("   STATISTICAL ANALYSIS COMPLETED")
print("======================================")