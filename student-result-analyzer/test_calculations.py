"""
test_calculations.py
Basic validation tests for the core logic (run directly with:  python test_calculations.py)
Demonstrates: functions, assertions, if-elif logic testing, and string/regex validators.
"""

from student_utils import calculate_grade, add_student, get_topper, count_pass_fail
from validators import is_valid_roll, is_valid_name, is_valid_mark, is_valid_email


def test_calculate_grade():
    assert calculate_grade(95) == "A+"
    assert calculate_grade(80) == "A"
    assert calculate_grade(65) == "B"
    assert calculate_grade(45) == "C"
    assert calculate_grade(20) == "F"
    print("test_calculate_grade passed")


def test_validators():
    assert is_valid_roll("21BCE1234") is True
    assert is_valid_roll("abcdefg") is False
    assert is_valid_name("Aravind Kumar") is True
    assert is_valid_name("Aravind123") is False
    assert is_valid_mark("87.5") is True
    assert is_valid_mark("150") is False
    assert is_valid_email("student@vit.edu") is True
    assert is_valid_email("not-an-email") is False
    print("test_validators passed")


def test_add_student_and_topper():
    students = []
    add_student(students, "21BCE1234", "Aravind", [90, 90, 90, 90, 90])
    add_student(students, "21BCE5678", "Meera", [40, 40, 40, 40, 40])

    assert len(students) == 2
    topper = get_topper(students)
    assert topper["name"] == "Aravind"

    pass_count, fail_count = count_pass_fail(students)
    assert pass_count == 2
    assert fail_count == 0
    print("test_add_student_and_topper passed")


if __name__ == "__main__":
    test_calculate_grade()
    test_validators()
    test_add_student_and_topper()
    print("\nAll tests passed successfully.")
