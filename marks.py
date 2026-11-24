# Student Marks Prediction System
def total_marks(marks):
    return sum(marks)
def percentage(marks):
    return sum(marks) / len(marks)
def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"
# Input
n = int(input("Enter number of subjects: "))
marks = []
for i in range(n):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
# Output
total = total_marks(marks)
per = percentage(marks)
student_grade = grade(per)
print("\n----- Student Result -----")
print("Total Marks =", total)
print("Percentage =", round(per, 2), "%")
print("Grade =", student_grade)
if per >= 40:
    print("Result = PASS")
else:
    print("Result = FAIL")