from validations import validate_mark
from calculations import calculate_total, calculate_average, calculate_grade
from display import display_result

def get_valid_mark(subject_number: int) -> float:
    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject_number}: "))
            if validate_mark(mark):
                return mark
            print("Invalid marks. Enter 0-100.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    name = input("Enter student name: ")
    marks = []

    for i in range(1, 4):
        mark = get_valid_mark(i)
        marks.append(mark)

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    display_result(name, total, average, grade)

if __name__ == "__main__":
    main()