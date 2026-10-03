def check_placement_eligibility(age, marks, attendance, experience, has_backlogs):
    if marks >= 60 and attendance >= 75 and not has_backlogs:
        eligibility = "Eligible"
    else:
        eligibility = "Not eligible"

    if marks >= 75 and not has_backlogs:
        marks_category = "Distinction"
    else:
        marks_category = "Regular"

    if experience == 0:
        experience_category = "Fresher"
    else:
        experience_category = "Experienced"

    return eligibility, marks_category, experience_category


age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
experience = float(input("Enter years of experience: "))
has_backlogs = input("Do you have backlogs? (yes/no): ").lower() == "yes"

eligibility, marks_category, experience_category = check_placement_eligibility(
    age, marks, attendance, experience, has_backlogs
)

print("Placement eligibility:", eligibility)
print("Marks category:", marks_category)
print("Experience category:", experience_category)