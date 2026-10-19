
import csv

print("STUDENT PERFORMANCE DATA ANALYZER")
print("----------------------------------")

students = []

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        math = int(row["Math"])
        science = int(row["Science"])
        english = int(row["English"])

        average = (math + science + english) / 3

        students.append({
            "name": name,
            "average": average
        })

        print(name, "- Average:", round(average, 2))

print("----------------------------------")

class_average = sum(
    student["average"] for student in students
) / len(students)

top_student = max(
    students, key=lambda student: student["average"]
)

print("Class Average:", round(class_average, 2))
print("Top Student:", top_student["name"])
print("Highest Average:", round(top_student["average"], 2))
