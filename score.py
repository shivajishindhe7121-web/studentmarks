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
def required_marks(target, current_marks, total_subjects):
    completed = len(current_marks)
    subjects_left = total_subjects - completed
    if subjects_left <= 0:
        return None
    marks_needed = (target * total_subjects) - sum(current_marks)
    return marks_needed / subjects_left
def main():
    n = int(input("Enter total number of subjects: "))
    completed = int(input("Enter completed subjects: "))
    if n <= 0 or completed <= 0 or completed > n:
        print("Invalid subject count")
        return
    marks = []
    for i in range(completed):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        if mark < 0 or mark > 100:
            print("Invalid marks. Enter marks between 0 and 100.")
            return
        marks.append(mark)
    total = total_marks(marks)
    per = percentage(marks)
    print("\n----- Student Result -----")
    print("Marks Obtained =", total)
    print("Current Percentage =", round(per, 2), "%")
    print("Current Grade =", grade(per))
    if completed < n:
        target = float(input("Enter target percentage: "))
        if target < 0 or target > 100:
            print("Invalid target percentage")
            return
        required = required_marks(target, marks, n)
        print("Required Average Marks =", round(required, 2))
        if required > 100:
            print("Target is not achievable")
        elif required <= 0:
            print("Target already achieved")
        else:
            print("Target can be achieved")
if __name__ == "__main__":
    main()