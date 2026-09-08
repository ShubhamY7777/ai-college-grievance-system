import pickle

# Load the saved AI model
with open("models/model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the text converter
with open("models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


print("========================================")
print("      COLLEGE GRIEVANCE AI")
print("========================================")

print("\nAI is ready!")
print("Type your complaint.")
print("Type 'exit' to stop.\n")


while True:

    complaint = input("Student Complaint: ")

    # Stop the program
    if complaint.lower() == "exit":
        print("\nThank you!")
        break

    # Convert complaint into numbers
    complaint_numbers = vectorizer.transform([complaint])

    # Ask AI for prediction
    prediction = model.predict(complaint_numbers)

    # Display result
    print("AI Department:", prediction[0])
    print("-" * 40)