import sqlite3


connection = sqlite3.connect(
    "database/complaints.db"
)

cursor = connection.cursor()


cursor.execute(
    "SELECT * FROM complaints"
)


complaints = cursor.fetchall()


print("\n========================================")
print("         ALL COMPLAINTS")
print("========================================")


for complaint in complaints:

    print("\nID:", complaint[0])

    print("Student:", complaint[1])

    print("Email:", complaint[2])

    print("Complaint:", complaint[3])

    print("Category:", complaint[4])

    print("Priority:", complaint[5])

    print("Status:", complaint[6])

    print("Created:", complaint[7])


connection.close()