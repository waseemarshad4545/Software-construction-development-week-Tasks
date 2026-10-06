
def calculate_total_and_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

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

def display_student_result(name, total, average, grade):
    print("\n" + "=" * 35)
    print(f"      STUDENT RESULT REPORT      ")
    print("=" * 35)
    print(f" Student Name : {name}")
    print(f" Total Marks  : {total}")
    print(f" Average      : {average:.2f}")
    print(f" Grade        : {grade}")
    print("=" * 35 + "\n")

def process_student(name, marks):
    total, average = calculate_total_and_average(marks)
    grade = determine_grade(average)
    display_student_result(name, total, average, grade)


if __name__ == "__main__":
    student_name = "Ahmad Khan"
    marks_list = [85, 78, 92, 88, 74]

    # Process student result
    process_student(student_name, marks_list)