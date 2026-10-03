def check_access(age, has_id, is_employee):
    if (age >= 18 and has_id) or is_employee:
        return "Access granted"
    return "Access denied"


age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"
is_employee = input("Are you an employee? (yes/no): ").lower() == "yes"

print(check_access(age, has_id, is_employee))