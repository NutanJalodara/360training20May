def calculate_percentage_and_grade(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 40:
        grade = 'E'
    else:
        grade = 'F'

    return percentage, grade

physics = float(input("Enter marks for Physics: "))
chemistry = float(input("Enter marks for Chemistry: "))
biology = float(input("Enter marks for Biology: "))
mathematics = float(input("Enter marks for Mathematics: "))
computer = float(input("Enter marks for Computer: "))
marks = [physics, chemistry, biology, mathematics, computer]
percentage, grade = calculate_percentage_and_grade(marks)
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
