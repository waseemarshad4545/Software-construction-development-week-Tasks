def calculate_total(marks: list[float]) -> float:
    return sum(marks)

def calculate_average(marks: list[float]) -> float:
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

def calculate_grade(average: float) -> str:
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