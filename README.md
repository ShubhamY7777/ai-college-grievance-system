# 🎓 AI College Grievance Redressal System

An **AI-powered College Grievance Redressal System** designed to simplify, automate, and improve the management of student complaints.

The system allows students to submit grievances through a web portal. Machine Learning analyzes the complaint and automatically predicts the appropriate college department. The complaint is then stored in a database for tracking and further processing.

> **7th Semester Major Project — Computer Science & Engineering**

---

## 📌 Project Overview

In many colleges, student complaints related to academics, examinations, accounts, hostel facilities, and infrastructure are handled manually through applications, emails, or verbal communication.

This can lead to:

* Delayed responses
* Complaints being sent to the wrong department
* Difficulty tracking complaint status
* Multiple students reporting the same issue
* Lack of accountability
* Complaints remaining unresolved for long periods

The **AI College Grievance Redressal System** aims to provide a centralized digital platform where students can submit complaints and track their resolution.

The system uses **Natural Language Processing (NLP)** and **Machine Learning** to automatically classify complaints and route them to the appropriate department.

---

# 🎯 Objectives

The main objectives of this project are:

1. Provide an online platform for students to submit grievances.
2. Automatically classify complaints using Machine Learning.
3. Route complaints to the appropriate college department.
4. Store complaints securely in a database.
5. Allow complaints to be tracked using their unique ID.
6. Provide administrators with a centralized complaint dashboard.
7. Assign priority levels to important complaints.
8. Detect duplicate or similar complaints.
9. Automatically escalate unresolved complaints after the defined SLA period.
10. Improve transparency and accountability in grievance management.

---

# ✨ Key Features

### 👨‍🎓 Student Features

* Submit a grievance online
* Enter student information
* Describe the problem
* Receive a unique complaint ID
* View predicted complaint department
* View complaint priority
* Track complaint status
* View complaint history

### 🤖 AI Features

* Automatic complaint classification
* NLP-based text processing
* Department prediction
* Priority/urgency detection
* Duplicate complaint detection
* Similar complaint identification

### 👨‍💼 Admin/Officer Features

* View all complaints
* Filter complaints by department
* Filter complaints by priority
* Update complaint status
* Add remarks
* Assign/reassign complaints
* Monitor unresolved complaints
* View escalated complaints
* Track grievance statistics

### ⏰ Escalation System

If a complaint remains unresolved beyond the defined SLA period, the system can automatically mark it as:

```text
ESCALATED
```

and make it visible to the higher authority.

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       STUDENT       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    WEB INTERFACE    │
                    │     HTML / CSS      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       FLASK         │
                    │    Backend Server    │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
       ┌─────────────────┐         ┌─────────────────┐
       │   AI / ML MODEL │         │     SQLITE      │
       │                 │         │    DATABASE     │
       │ TF-IDF          │         │                 │
       │       +         │         │ Complaints      │
       │ Naive Bayes     │         │ Students        │
       └────────┬────────┘         │ Status          │
                │                  │ Priority        │
                ▼                  └─────────────────┘
        Department Prediction
```

---

# 🔄 Complaint Processing Workflow

```text
Student submits complaint
            ↓
       Flask receives data
            ↓
      Text preprocessing
            ↓
       TF-IDF conversion
            ↓
      Machine Learning model
            ↓
     Department prediction
            ↓
       Priority assignment
            ↓
       Database storage
            ↓
      Officer/Admin review
            ↓
      Status updated
            ↓
        Complaint resolved
```

---

# 🧠 Machine Learning

The current prototype uses a supervised Machine Learning approach.

## Text Feature Extraction

The complaint text is converted into numerical features using:

**TF-IDF — Term Frequency-Inverse Document Frequency**

Example:

```text
"The hostel fan is not working"
```

is converted into numerical features that the Machine Learning algorithm can process.

---

## Classification Algorithm

The current prototype uses:

**Multinomial Naive Bayes**

The model learns relationships between complaint text and predefined departments.

### Current Categories

```text
Hostel
Academics
Accounts
Maintenance
```

Example:

```text
Input:
"The fan in my hostel room is broken."

Output:
Hostel
```

Another example:

```text
Input:
"My semester fee was deducted twice."

Output:
Accounts
```

---

# 🗃️ Database

The application currently uses **SQLite** for local database storage.

The complaint table contains information such as:

| Field          | Description               |
| -------------- | ------------------------- |
| ID             | Unique complaint ID       |
| Student Name   | Name of student           |
| Student Email  | Student email             |
| Complaint Text | Submitted grievance       |
| Category       | AI predicted department   |
| Priority       | Complaint priority        |
| Status         | Current complaint status  |
| Created At     | Complaint submission time |

---

# 🛠️ Technology Stack

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask

## Machine Learning

* Python
* Pandas
* Scikit-learn
* TF-IDF
* Multinomial Naive Bayes

## Database

* SQLite

## Development Tools

* Visual Studio Code
* Git
* GitHub

---

# 📂 Project Structure

```text
Grievance_Project/
│
├── data/
│   └── complaints.csv
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│
├── database/
│   └── complaints.db
│
├── venv/
│
├── app.py
├── train.py
├── test_model.py
├── view_database.py
├── requirements.txt
├── .gitignore
└── README.md
```

> Generated model files, the local database, and the Python virtual environment should not be committed to GitHub. They can be recreated locally.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-college-grievance-system.git
```

Move into the project:

```bash
cd ai-college-grievance-system
```

---

## 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

Windows Command Prompt:

```cmd
venv\Scripts\activate
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Train the Machine Learning Model

Before running the application, train the model:

```bash
python train.py
```

After successful training, the following files will be created:

```text
models/
├── model.pkl
└── vectorizer.pkl
```

---

# ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

You should see:

```text
Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🧪 Testing the AI

You can test the trained model independently using:

```bash
python test_model.py
```

Example:

```text
Student Complaint:
My hostel room fan is broken

AI Department:
Hostel
```

Another example:

```text
Student Complaint:
My semester fee was deducted twice

AI Department:
Accounts
```

---

# 📊 Example Use Cases

### Example 1 — Hostel

```text
Complaint:
"The water supply in my hostel bathroom is not working."

AI Prediction:
Hostel
```

### Example 2 — Accounts

```text
Complaint:
"My college fee was deducted twice from my bank account."

AI Prediction:
Accounts
```

### Example 3 — Maintenance

```text
Complaint:
"The projector in the computer laboratory is not working."

AI Prediction:
Maintenance
```

### Example 4 — Academics

```text
Complaint:
"My semester result contains incorrect marks."

AI Prediction:
Academics
```

---

# 🔐 Security Considerations

Future versions of the project will include:

* User authentication
* Role-based access control
* Password hashing
* Input validation
* Secure session management
* Protection of student information
* File upload validation
* API security

---

# 🚀 Future Enhancements

The current system is a prototype and can be extended with:

### 1. Advanced NLP

Replace the basic classifier with:

* BERT
* DistilBERT
* Sentence Transformers

### 2. Duplicate Complaint Detection

Use text embeddings and cosine similarity to identify complaints describing the same issue.

Example:

```text
Student 1:
"WiFi is not working on the third floor."

Student 2:
"Third floor hostel internet is down."

Student 3:
"No internet connection in hostel floor 3."
```

The system can identify these as potentially related complaints.

### 3. Automatic Priority Detection

The system can classify complaints as:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

For example:

```text
"Room fan makes a little noise."
→ LOW/MEDIUM

"Electrical panel is producing sparks."
→ CRITICAL
```

### 4. Automatic Escalation

Unresolved complaints can automatically be escalated after the defined SLA period.

### 5. Email Notifications

Students and officers can receive notifications when:

* Complaint is submitted
* Complaint is assigned
* Status changes
* Complaint is resolved
* Complaint is escalated

### 6. Admin Analytics

Add dashboards showing:

* Total complaints
* Open complaints
* Resolved complaints
* Escalated complaints
* Department-wise complaints
* Priority distribution
* Average resolution time

### 7. Production Database

SQLite can eventually be replaced with:

```text
PostgreSQL
```

for a larger deployment.

---

# 📈 Future Architecture

```text
                    STUDENT
                       │
                       ▼
               React / Web App
                       │
                       ▼
                  REST API
                       │
                       ▼
              Python Backend
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       AI/ML        Database      Storage
       Service      PostgreSQL    Documents
          │
     ┌────┼──────────────┐
     │    │              │
     ▼    ▼              ▼
Category Priority    Duplicate
Routing  Detection   Detection
     │
     └──────────┬─────────┘
                ▼
          Complaint
          Management
                │
                ▼
          SLA Monitoring
                │
                ▼
            Escalation
```

---

# 📚 Learning Objectives

This project is also intended to provide practical experience with:

* Python programming
* Web development
* Flask
* HTML/CSS
* Databases
* SQL
* Machine Learning
* Natural Language Processing
* Text classification
* Model evaluation
* Git and GitHub
* Software development
* System design

---

# 🎓 Academic Relevance

This project demonstrates the application of Artificial Intelligence and Machine Learning to a practical institutional problem.

It combines:

```text
Web Development
       +
Python
       +
Machine Learning
       +
NLP
       +
Database
       +
Workflow Automation
```

The project is intended as a **7th-semester Computer Science and Engineering major project**.

---

# 🧑‍💻 Project Development Status

| Module                   | Status            |
| ------------------------ | ----------------- |
| Project Setup            | ✅ Completed       |
| Training Dataset         | ✅ Completed       |
| ML Classifier            | ✅ Completed       |
| AI Testing               | ✅ Completed       |
| Flask Website            | ✅ Completed       |
| SQLite Database          | ✅ Completed       |
| AI + Website Integration | ✅ Completed       |
| Student Dashboard        | 🔄 In Development |
| Admin Dashboard          | 🔄 Planned        |
| Priority Detection       | 🔄 Planned        |
| Duplicate Detection      | 🔄 Planned        |
| SLA Escalation           | 🔄 Planned        |
| Notifications            | 🔄 Planned        |
| Final Analytics          | 🔄 Planned        |

---

# 👨‍🎓 Project Team

**Student:** Shubham Yadav
**Course:** Bachelor of Technology — Computer Science and Engineering
**Semester:** 7th Semester
**Project Type:** Major Project

---

# 📜 License

This project is developed for educational and academic purposes.

---

# ⭐ Acknowledgement

This project was developed as an academic project to explore the practical application of Artificial Intelligence, Machine Learning, Natural Language Processing, web development, and database technologies to college grievance management.

---

## ⭐ If you find this project useful

Consider giving the repository a ⭐ on GitHub.
