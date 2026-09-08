import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

print("========================================")
print("   AI COLLEGE GRIEVANCE SYSTEM")
print("========================================")

# 1. Read the dataset
print("\n1. Reading training data...")

df = pd.read_csv("data/complaints.csv")

print("Total complaints:", len(df))
print("Categories:", df["category"].unique())


# 2. Convert text into numbers
print("\n2. Converting text into numbers...")

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["text"])

y = df["category"]


# 3. Train the machine learning model
print("\n3. Training AI model...")

model = MultinomialNB()

model.fit(X, y)


# 4. Create models folder
os.makedirs("models", exist_ok=True)


# 5. Save vectorizer
print("\n4. Saving vectorizer...")

with open("models/vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)


# 6. Save trained model
print("5. Saving AI model...")

with open("models/model.pkl", "wb") as file:
    pickle.dump(model, file)


print("\n========================================")
print("       AI TRAINING COMPLETED!")
print("========================================")

print("\nModel saved successfully.")

print("\nFiles created:")
print("models/model.pkl")
print("models/vectorizer.pkl")


# 7. Test the AI
print("\n========================================")
print("           TESTING AI")
print("========================================")

test_complaints = [
    "My hostel fan is broken",
    "My college fee was deducted twice",
    "The projector in my laboratory is not working",
    "My examination marks are incorrect"
]

test_numbers = vectorizer.transform(test_complaints)

predictions = model.predict(test_numbers)


for complaint, prediction in zip(test_complaints, predictions):

    print("\nComplaint:", complaint)
    print("AI Prediction:", prediction)


print("\n========================================")
print("          PROJECT STEP 2 DONE")
print("========================================")