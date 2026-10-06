# ==========================================
# Task 1: Refactor Student Result Program
# Principles Applied: Single Responsibility Principle (SRP)
# ==========================================

# 1. Calculation Logic: Responsibly calculates total and average marks
def calculate_total_and_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


# 2. Decision Logic: Determines grade based on average score
def determine_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# 3. Presentation Logic: Handles console output formatting
def display_student_result(name, total, average, grade):
    print("\n" + "=" * 35)
    print(f"      STUDENT RESULT REPORT      ")
    print("=" * 35)
    print(f" Student Name : {name}")
    print(f" Total Marks  : {total}")
    print(f" Average      : {average:.2f}")
    print(f" Grade        : {grade}")
    print("=" * 35 + "\n")


# Main Orchestration Function
def process_student(name, marks):
    total, average = calculate_total_and_average(marks)
    grade = determine_grade(average)
    display_student_result(name, total, average, grade)


# Execution Entry Point
if __name__ == "__main__":
    student_name = "Ahmad Khan"
    marks_list = [85, 78, 92, 88, 74]

    # Process student result
    process_student(student_name, marks_list)