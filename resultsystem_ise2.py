import pandas as pd

def grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"
    else:
        return "F"

n = int(input("Enter number of students: "))
data = []

for i in range(n):

    roll = input("Enter roll no: ")
    name = input("Enter name: ")

    marks = int(input("Enter marks: "))
    g = grade(marks)
    data.append([roll, name, marks, g])

df = pd.DataFrame(data, columns=["Roll No", "Name", "Marks", "Grade"])

df.to_csv("students.csv", index=False)
print("\nStudent Records:")
print(df)


topper = df.loc[df["Marks"].idxmax()]
print("\nTopper:")

print("Name:", topper["Name"])
print("Marks:", topper["Marks"])

print("\nStatistics:")
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
