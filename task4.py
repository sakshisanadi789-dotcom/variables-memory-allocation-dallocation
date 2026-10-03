def check_eligibility(marks, attendance, backlog_status):
    if marks >= 60 and attendance >= 75 and backlog_status.lower() == "fail":
        return "eligible"
    return "noteligible"


marks = int(input("Enter the student's marks: "))
attendance = int(input("Enter the student's attendance percentage: "))
backlog_status = input("Enter the backlog status (fail/pass): ")

result = check_eligibility(marks, attendance, backlog_status)
print(result)
