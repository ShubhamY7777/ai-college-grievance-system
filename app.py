from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
import pickle
import os


app = Flask(__name__)


# =========================================
# FILE PATHS
# =========================================

DATABASE_FOLDER = "database"
DATABASE_PATH = os.path.join(
    DATABASE_FOLDER,
    "complaints.db"
)

MODEL_PATH = "models/model.pkl"

VECTORIZER_PATH = "models/vectorizer.pkl"


# =========================================
# LOAD AI MODEL
# =========================================

print("Loading AI model...")


with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


with open(VECTORIZER_PATH, "rb") as file:
    vectorizer = pickle.load(file)


print("AI model loaded successfully!")


# =========================================
# CREATE DATABASE
# =========================================

def create_database():

    os.makedirs(
        DATABASE_FOLDER,
        exist_ok=True
    )

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_name TEXT NOT NULL,

            student_email TEXT NOT NULL,

            complaint_text TEXT NOT NULL,

            category TEXT,

            priority TEXT DEFAULT 'Medium',

            status TEXT DEFAULT 'Open',

            created_at TEXT NOT NULL

        )
    """)


    connection.commit()

    connection.close()


# =========================================
# HOME PAGE
# =========================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# =========================================
# SUBMIT COMPLAINT
# =========================================

@app.route(
    "/submit",
    methods=["POST"]
)
def submit_complaint():

    # -------------------------------------
    # Get student information
    # -------------------------------------

    student_name = request.form[
        "student_name"
    ]

    student_email = request.form[
        "student_email"
    ]

    complaint_text = request.form[
        "complaint_text"
    ]


    # -------------------------------------
    # AI PREDICTION
    # -------------------------------------

    complaint_numbers = vectorizer.transform(
        [complaint_text]
    )


    prediction = model.predict(
        complaint_numbers
    )


    predicted_category = prediction[0]


    # -------------------------------------
    # Current date and time
    # -------------------------------------

    created_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    # -------------------------------------
    # Save to database
    # -------------------------------------

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()


    cursor.execute("""
        INSERT INTO complaints
        (
            student_name,
            student_email,
            complaint_text,
            category,
            priority,
            status,
            created_at
        )

        VALUES (?, ?, ?, ?, ?, ?, ?)

    """, (

        student_name,

        student_email,

        complaint_text,

        predicted_category,

        "Medium",

        "Open",

        created_at

    ))


    connection.commit()


    complaint_id = cursor.lastrowid


    connection.close()


    # -------------------------------------
    # Display information in terminal
    # -------------------------------------

    print("\n========================================")

    print("       NEW GRIEVANCE")

    print("========================================")

    print(
        "Complaint ID:",
        complaint_id
    )

    print(
        "Student:",
        student_name
    )

    print(
        "Email:",
        student_email
    )

    print(
        "Complaint:",
        complaint_text
    )

    print(
        "AI Category:",
        predicted_category
    )

    print(
        "Priority: Medium"
    )

    print(
        "Status: Open"
    )

    print("========================================\n")


    # -------------------------------------
    # Show result to student
    # -------------------------------------

    return f"""

    <!DOCTYPE html>

    <html>

    <head>

        <title>
            Complaint Submitted
        </title>

    </head>


    <body style="
        font-family: Arial;
        background: #f4f7fb;
        padding: 60px;
    ">


        <div style="
            background: white;
            max-width: 650px;
            margin: auto;
            padding: 40px;
            border-radius: 12px;
            text-align: center;
        ">


            <h1 style="
                color: green;
            ">

                Complaint Submitted Successfully!

            </h1>


            <br>


            <h3>

                Complaint ID:
                #{complaint_id}

            </h3>


            <br>


            <p>

                <strong>
                    Student:
                </strong>

                {student_name}

            </p>


            <p>

                <strong>
                    AI Department:
                </strong>

                {predicted_category}

            </p>


            <p>

                <strong>
                    Priority:
                </strong>

                Medium

            </p>


            <p>

                <strong>
                    Status:
                </strong>

                Open

            </p>


            <br>


            <div style="
                background: #eef4ff;
                padding: 20px;
                border-radius: 8px;
            ">

                <strong>
                    Your complaint has been
                    automatically routed to:
                </strong>

                <br><br>

                {predicted_category}

            </div>


            <br>


            <a href="/">

                Submit Another Complaint

            </a>


        </div>


    </body>

    </html>

    """


# =========================================
# START APPLICATION
# =========================================

if __name__ == "__main__":

    create_database()


    print(
        "========================================"
    )

    print(
        " AI COLLEGE GRIEVANCE SYSTEM"
    )

    print(
        "========================================"
    )


    app.run(
        debug=True
    )