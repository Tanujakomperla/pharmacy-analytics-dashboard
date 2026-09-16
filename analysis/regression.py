import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Excel file
file_path = r"C:\Users\Tanuja\Desktop\Pharmacy_Analytics_Dashboard\data\Pharmacy_Student_Performance_Dataset.xlsx"

# Read data
df = pd.read_excel(file_path)

# Clean data
df = df.drop_duplicates()
df = df.dropna()

# Features
X = df[
    [
        "Attendance_%",
        "Study_Hours_Per_Day",
        "Internal_Average"
    ]
]

# Target
y = df["Final_Marks"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create regression model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print("\n======================================")
print("       REGRESSION ANALYSIS")
print("======================================")

print("\nFeatures used:")
print("- Attendance")
print("- Study Hours")
print("- Internal Average")

print("\nTarget:")
print("- Final Marks")

print("\nModel Performance")
print("--------------------------------")
print("R² Score:", round(r2, 3))
print("MAE:", round(mae, 3))
print("MSE:", round(mse, 3))
print("RMSE:", round(rmse, 3))

print("\nModel Coefficients")
print("--------------------------------")
print("Attendance:", round(model.coef_[0], 3))
print("Study Hours:", round(model.coef_[1], 3))
print("Internal Average:", round(model.coef_[2], 3))
print("Intercept:", round(model.intercept_, 3))

print("\nActual vs Predicted")
print("--------------------------------")

results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred.round(2)
})

print(results)

print("\n======================================")
print("      REGRESSION ANALYSIS COMPLETED")
print("======================================")