"""
student_utils.py
Custom module holding all student-record and grade-calculation logic.
Demonstrates: lists, dictionaries, tuples, functions (required,
default, variable-length, lambda), loops, and if-elif control flow.
"""

SUBJECTS = ("Maths", "Physics", "Chemistry", "Python", "English")  # tuple - fixed subject list


def add_student(students, roll, name, marks):
    """
    Adds a new student record to the 'students' list.
    'students' -> list of dictionaries (one dict per student)
    'marks'    -> list of 5 numeric marks
    """
    total = sum(marks)                       # built-in sum() on a list
    percentage = total / len(marks)
    grade = calculate_grade(percentage)

    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
    }
    students.append(student)
    return student


def calculate_grade(percentage, pass_mark=40):
    """
    Determines grade using if-elif ladder.
    'pass_mark' is a default argument.
    """
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= pass_mark:
        return "C"
    else:
        return "F"


def search_student(students, roll):
    """
    Linear search through the list using a for loop + break-style return.
    """
    for s in students:
        if s["roll"] == roll:
            return s
    return None


def get_topper(students):
    """
    Uses a lambda function as the sort key to find the topper.
    """
    if not students:
        return None
    return sorted(students, key=lambda s: s["percentage"], reverse=True)[0]


def count_pass_fail(students):
    """
    Iterates the list once, using if-else to classify pass/fail.
    Returns a tuple (pass_count, fail_count).
    """
    pass_count = 0
    fail_count = 0
    for s in students:
        if s["grade"] != "F":
            pass_count += 1
        else:
            fail_count += 1
    return (pass_count, fail_count)          # tuple return


def class_average(students, *subjects_index):
    """
    Variable-length argument function.
    If specific subject indexes are passed, averages only those subjects
    across all students; otherwise averages overall percentage.
    """
    if not students:
        return 0
    if subjects_index:
        total = 0
        count = 0
        for s in students:
            for idx in subjects_index:
                total += s["marks"][idx]
                count += 1
        return total / count
    else:
        return sum(s["percentage"] for s in students) / len(students)


def sort_students_by_rank(students):
    """
    Returns a new list of students sorted by percentage (descending)
    using a lambda key function.
    """
    return sorted(students, key=lambda s: s["percentage"], reverse=True)
