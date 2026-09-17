from flask import Flask, render_template, request
import pandas as pd
import os
import numpy as np

app = Flask(__name__)


# ---------------------------------------------------
# PROJECT AND EXCEL FILE PATH
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    BASE_DIR,
    "data",
    "Pharmacy_Student_Performance_Dataset.xlsx"
)


# ---------------------------------------------------
# HOME PAGE - INTERACTIVE DASHBOARD
# ---------------------------------------------------

@app.route("/")
def home():

    # Read Excel file
    df = pd.read_excel(file_path)

    # Clean data
    df = df.drop_duplicates()
    df = df.dropna()

    # Convert data into records for JavaScript
    students = df.to_dict(orient="records")

    # ------------------------------------------------
    # MAIN DASHBOARD VALUES
    # ------------------------------------------------

    total_students = len(df)

    average_attendance = round(
        df["Attendance_%"].mean(), 2
    )

    average_study_hours = round(
        df["Study_Hours_Per_Day"].mean(), 2
    )

    average_final_marks = round(
        df["Final_Marks"].mean(), 2
    )

    highest_marks = round(
        df["Final_Marks"].max(), 2
    )

    lowest_marks = round(
        df["Final_Marks"].min(), 2
    )

    # ------------------------------------------------
    # PASS PERCENTAGE
    # ------------------------------------------------

    pass_count = (
        df["Status"]
        .astype(str)
        .str.lower()
        .eq("pass")
        .sum()
    )

    pass_percentage = round(
        (pass_count / total_students) * 100,
        2
    )

    # ------------------------------------------------
    # SUBJECT AVERAGES
    # ------------------------------------------------

    pharmacology_average = round(
        df["Pharmacology"].mean(), 2
    )

    pharmaceutics_average = round(
        df["Pharmaceutics"].mean(), 2
    )

    pharmacognosy_average = round(
        df["Pharmacognosy"].mean(), 2
    )

    # ------------------------------------------------
    # RENDER INTERACTIVE DASHBOARD
    # ------------------------------------------------

    return render_template(
        "index.html",

        total_students=total_students,

        average_attendance=average_attendance,

        average_study_hours=average_study_hours,

        average_final_marks=average_final_marks,

        highest_marks=highest_marks,

        lowest_marks=lowest_marks,

        pass_percentage=pass_percentage,

        pharmacology_average=pharmacology_average,

        pharmaceutics_average=pharmaceutics_average,

        pharmacognosy_average=pharmacognosy_average,

        students=students,

        subject_labels=[
            "Pharmacology",
            "Pharmaceutics",
            "Pharmacognosy"
        ],

        subject_values=[
            pharmacology_average,
            pharmaceutics_average,
            pharmacognosy_average
        ]
    )


# ---------------------------------------------------
# ACADEMIC ANALYSIS PAGE
# ---------------------------------------------------

@app.route("/academic-analysis")
def academic_analysis():

    # Read Excel file
    df = pd.read_excel(file_path)

    # Clean data
    df = df.drop_duplicates()
    df = df.dropna()

    # Subject averages
    pharmacology_average = round(
        df["Pharmacology"].mean(),
        2
    )

    pharmaceutics_average = round(
        df["Pharmaceutics"].mean(),
        2
    )

    pharmacognosy_average = round(
        df["Pharmacognosy"].mean(),
        2
    )

    # ------------------------------------------------
    # OVERALL SUBJECT AVERAGE
    # ------------------------------------------------

    overall_subject_average = round(
        df[
            [
                "Pharmacology",
                "Pharmaceutics",
                "Pharmacognosy"
            ]
        ].mean().mean(),
        2
    )

    # ------------------------------------------------
    # HIGHEST AND LOWEST MARKS
    # ------------------------------------------------

    highest_marks = round(
        df["Final_Marks"].max(),
        2
    )

    lowest_marks = round(
        df["Final_Marks"].min(),
        2
    )

    return render_template(
        "academic_analysis.html",

        pharmacology_average=pharmacology_average,

        pharmaceutics_average=pharmaceutics_average,

        pharmacognosy_average=pharmacognosy_average,

        overall_subject_average=overall_subject_average,

        highest_marks=highest_marks,

        lowest_marks=lowest_marks,

        students=df.to_dict(
            orient="records"
        )
    )


# ---------------------------------------------------
# CORRELATION PAGE
# ---------------------------------------------------

@app.route("/correlation")
def correlation():

    # Read Excel file
    df = pd.read_excel(file_path)

    # Clean data
    df = df.drop_duplicates()
    df = df.dropna()

    # ------------------------------------------------
    # CALCULATE CORRELATION WITH FINAL MARKS
    # ------------------------------------------------

    correlation_values = {

        "Attendance": round(
            df["Attendance_%"].corr(
                df["Final_Marks"]
            ),
            3
        ),

        "Study Hours": round(
            df["Study_Hours_Per_Day"].corr(
                df["Final_Marks"]
            ),
            3
        ),

        "Pharmacology": round(
            df["Pharmacology"].corr(
                df["Final_Marks"]
            ),
            3
        ),

        "Pharmaceutics": round(
            df["Pharmaceutics"].corr(
                df["Final_Marks"]
            ),
            3
        ),

        "Pharmacognosy": round(
            df["Pharmacognosy"].corr(
                df["Final_Marks"]
            ),
            3
        ),

        "Internal Average": round(
            df["Internal_Average"].corr(
                df["Final_Marks"]
            ),
            3
        )
    }

    return render_template(

        "correlation.html",

        # Send student records for
        # interactive filtering
        students=df.to_dict(
            orient="records"
        ),

        correlation_labels=list(
            correlation_values.keys()
        ),

        correlation_values=list(
            correlation_values.values()
        ),

        attendance_corr=correlation_values[
            "Attendance"
        ],

        study_hours_corr=correlation_values[
            "Study Hours"
        ],

        pharmacology_corr=correlation_values[
            "Pharmacology"
        ],

        pharmaceutics_corr=correlation_values[
            "Pharmaceutics"
        ],

        pharmacognosy_corr=correlation_values[
            "Pharmacognosy"
        ],

        internal_average_corr=correlation_values[
            "Internal Average"
        ]
    )


# ---------------------------------------------------
# STATISTICS PAGE
# ---------------------------------------------------

@app.route("/statistics")
def statistics():

    # Read Excel file
    df = pd.read_excel(file_path)

    # Clean data
    df = df.drop_duplicates()
    df = df.dropna()

    # ------------------------------------------------
    # COLUMNS FOR STATISTICAL ANALYSIS
    # ------------------------------------------------

    columns = [

        "Attendance_%",

        "Study_Hours_Per_Day",

        "Pharmacology",

        "Pharmaceutics",

        "Pharmacognosy",

        "Internal_Average",

        "Final_Marks"
    ]

    # ------------------------------------------------
    # ORIGINAL STATISTICS
    # ------------------------------------------------

    statistics_data = {}

    for column in columns:

        statistics_data[column] = {

            "mean": round(
                df[column].mean(),
                2
            ),

            "median": round(
                df[column].median(),
                2
            ),

            "std": round(
                df[column].std(),
                2
            ),

            "min": round(
                df[column].min(),
                2
            ),

            "max": round(
                df[column].max(),
                2
            )
        }

    # ------------------------------------------------
    # RENDER STATISTICS PAGE
    # ------------------------------------------------

    return render_template(

        "statistics.html",

        statistics_data=statistics_data,

        # Send student data to JavaScript
        # for live filtering and calculations.
        students=df.to_dict(
            orient="records"
        )
    )


# ---------------------------------------------------
# PREDICTION PAGE
# ---------------------------------------------------

@app.route(
    "/prediction",
    methods=["GET", "POST"]
)
def prediction():

    from sklearn.model_selection import train_test_split

    from sklearn.linear_model import LinearRegression

    from sklearn.metrics import (
        r2_score,
        mean_absolute_error,
        mean_squared_error
    )

    # Read Excel file
    df = pd.read_excel(file_path)

    # Clean data
    df = df.drop_duplicates()
    df = df.dropna()

    # ------------------------------------------------
    # FEATURES AND TARGET
    # ------------------------------------------------

    X = df[
        [
            "Attendance_%",
            "Study_Hours_Per_Day",
            "Internal_Average"
        ]
    ]

    y = df["Final_Marks"]

    # ------------------------------------------------
    # TRAIN TEST SPLIT
    # ------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42
    )

    # ------------------------------------------------
    # TRAIN MODEL
    # ------------------------------------------------

    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )

    # ------------------------------------------------
    # MODEL PREDICTIONS
    # ------------------------------------------------

    y_pred = model.predict(
        X_test
    )

    # ------------------------------------------------
    # MODEL EVALUATION
    # ------------------------------------------------

    r2 = round(
        r2_score(
            y_test,
            y_pred
        ),
        3
    )

    mae = round(
        mean_absolute_error(
            y_test,
            y_pred
        ),
        3
    )

    # Calculate raw MSE first
    mse_raw = mean_squared_error(
        y_test,
        y_pred
    )

    mse = round(
        mse_raw,
        3
    )

    rmse = round(
        np.sqrt(mse_raw),
        3
    )

    # ------------------------------------------------
    # ACTUAL VS PREDICTED
    # ------------------------------------------------

    actual_values = [

        round(
            float(value),
            2
        )

        for value in y_test
    ]

    predicted_values = [

        round(
            float(value),
            2
        )

        for value in y_pred
    ]

    # ------------------------------------------------
    # DEFAULT USER PREDICTION
    # ------------------------------------------------

    predicted_mark = None

    # ------------------------------------------------
    # USER INPUT PREDICTION
    # ------------------------------------------------

    if request.method == "POST":

        attendance = float(
            request.form["attendance"]
        )

        study_hours = float(
            request.form["study_hours"]
        )

        internal_average = float(
            request.form["internal_average"]
        )

        # Create DataFrame with feature names
        user_input = pd.DataFrame(

            [[
                attendance,
                study_hours,
                internal_average
            ]],

            columns=[
                "Attendance_%",
                "Study_Hours_Per_Day",
                "Internal_Average"
            ]
        )

        prediction_result = model.predict(
            user_input
        )

        predicted_mark = round(
            float(prediction_result[0]),
            2
        )

    # ------------------------------------------------
    # RENDER PAGE
    # ------------------------------------------------

    return render_template(

        "prediction.html",

        r2=r2,

        mae=mae,

        mse=mse,

        rmse=rmse,

        actual_values=actual_values,

        predicted_values=predicted_values,

        predicted_mark=predicted_mark,

        # NEW:
        # Send all student records to
        # prediction.html for interactive
        # student selection.
        students=df.to_dict(
            orient="records"
        )
    )


# ---------------------------------------------------
# INSIGHTS PAGE
# ---------------------------------------------------

@app.route("/insights")
def insights():

    # Read Excel file
    df = pd.read_excel(file_path)

    # Clean data
    df = df.drop_duplicates()
    df = df.dropna()

    # ------------------------------------------------
    # BASIC VALUES
    # ------------------------------------------------

    total_students = len(df)

    average_attendance = round(
        df["Attendance_%"].mean(),
        2
    )

    average_study_hours = round(
        df["Study_Hours_Per_Day"].mean(),
        2
    )

    average_final_marks = round(
        df["Final_Marks"].mean(),
        2
    )

    highest_marks = round(
        df["Final_Marks"].max(),
        2
    )

    lowest_marks = round(
        df["Final_Marks"].min(),
        2
    )

    # ------------------------------------------------
    # SUBJECT AVERAGES
    # ------------------------------------------------

    pharmacology_average = round(
        df["Pharmacology"].mean(),
        2
    )

    pharmaceutics_average = round(
        df["Pharmaceutics"].mean(),
        2
    )

    pharmacognosy_average = round(
        df["Pharmacognosy"].mean(),
        2
    )

    # ------------------------------------------------
    # OVERALL SUBJECT AVERAGE
    # ------------------------------------------------

    overall_subject_average = round(
        df[
            [
                "Pharmacology",
                "Pharmaceutics",
                "Pharmacognosy"
            ]
        ].mean().mean(),
        2
    )

    # ------------------------------------------------
    # CORRELATIONS
    # ------------------------------------------------

    attendance_corr = round(
        df["Attendance_%"].corr(
            df["Final_Marks"]
        ),
        3
    )

    study_hours_corr = round(
        df["Study_Hours_Per_Day"].corr(
            df["Final_Marks"]
        ),
        3
    )

    pharmacognosy_corr = round(
        df["Pharmacognosy"].corr(
            df["Final_Marks"]
        ),
        3
    )

    internal_average_corr = round(
        df["Internal_Average"].corr(
            df["Final_Marks"]
        ),
        3
    )

    # ------------------------------------------------
    # HIGHEST AVERAGE SUBJECT
    # ------------------------------------------------

    subject_averages = {

        "Pharmacology":
            pharmacology_average,

        "Pharmaceutics":
            pharmaceutics_average,

        "Pharmacognosy":
            pharmacognosy_average
    }

    highest_subject = max(
        subject_averages,
        key=subject_averages.get
    )

    highest_subject_average = (
        subject_averages[
            highest_subject
        ]
    )

    # ------------------------------------------------
    # RENDER INSIGHTS PAGE
    # ------------------------------------------------

    return render_template(

        "insights.html",

        total_students=total_students,

        average_attendance=average_attendance,

        average_study_hours=average_study_hours,

        average_final_marks=average_final_marks,

        pharmacology_average=pharmacology_average,

        pharmaceutics_average=pharmaceutics_average,

        pharmacognosy_average=pharmacognosy_average,

        overall_subject_average=overall_subject_average,

        highest_subject=highest_subject,

        highest_subject_average=highest_subject_average,

        highest_marks=highest_marks,

        lowest_marks=lowest_marks,

        attendance_corr=attendance_corr,

        study_hours_corr=study_hours_corr,

        pharmacognosy_corr=pharmacognosy_corr,

        internal_average_corr=internal_average_corr,

        students=df.to_dict(
            orient="records"
        )
    )


# ---------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )