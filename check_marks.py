def check_marks(marks):
    if marks >= 75:
        return "Distinction"
    if marks >= 35:
        return "Pass"
    return "Fail"


marks = int(input("Enter the student's marks: "))
result = check_marks(marks)
print(result)
