def calculate_grade(grades):
    average = sum(grades) / len(grades)
    return "Pass" if average >= 60 else "Fail"

grades = [float(input("Enter grade: ")) for _ in range(5)]
status = calculate_grade(grades)
print(f"Average grade: {sum(grades) / len(grades)}")
print(f"Status: {status}")
