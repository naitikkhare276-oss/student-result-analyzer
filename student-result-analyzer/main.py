"""
main.py
Entry point of the Student Result & Grade Analyzer.
Demonstrates: while loop, if-elif-else control statements,
break/continue/pass, module import, and function calls.
"""

from student_utils import (
    add_student,
    search_student,
    get_topper,
    count_pass_fail,
    class_average,
    sort_students_by_rank,
    SUBJECTS,
)
from validators import is_valid_roll, is_valid_name, is_valid_mark
import report

students = []   # global list of dictionaries - holds all student records


def get_valid_marks():
    """Repeatedly prompts until 5 valid marks are entered."""
    marks = []
    for subject in SUBJECTS:
        while True:
            mark_str = input(f"Enter marks for {subject} (0-100): ")
            if is_valid_mark(mark_str):
                marks.append(float(mark_str))
                break                       # break out of the inner while loop
            else:
                print("Invalid mark. Please enter a number between 0 and 100.")
    return marks


def menu_add_student():
    roll = input("Enter Roll Number (e.g., 21BCE1234): ").strip().upper()
    if not is_valid_roll(roll):
        print("Invalid roll number format. Expected format: 21BCE1234")
        return

    name = input("Enter Student Name: ").strip()
    if not is_valid_name(name):
        print("Invalid name. Only alphabets and spaces are allowed.")
        return

    if search_student(students, roll) is not None:
        print("A student with this roll number already exists.")
        return

    marks = get_valid_marks()
    student = add_student(students, roll, name, marks)
    print(f"\nStudent '{student['name']}' added successfully with grade {student['grade']}.")


def menu_view_all():
    report.print_all_students(students)


def menu_search_student():
    roll = input("Enter Roll Number to search: ").strip().upper()
    student = search_student(students, roll)
    if student is None:
        print("No student found with that roll number.")
    else:
        report.print_report_card(student)


def menu_analytics():
    if not students:
        print("\nNo records available for analytics.")
        return
    topper = get_topper(students)
    pass_count, fail_count = count_pass_fail(students)
    avg = class_average(students)
    report.print_analytics(students, topper, pass_count, fail_count, avg)


def menu_ranked_list():
    ranked = sort_students_by_rank(students)
    if not ranked:
        print("\nNo records to rank.")
        return
    report.print_header("STUDENTS RANKED BY PERCENTAGE")
    for position, s in enumerate(ranked, start=1):
        print(f"{position}. {s['name']} ({s['roll']}) - {s['percentage']:.2f}%")


def show_menu():
    print("\n" + "=" * 40)
    print("   STUDENT RESULT & GRADE ANALYZER")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll Number")
    print("4. View Class Analytics")
    print("5. View Ranked List (Toppers first)")
    print("6. Exit")


def main():
    while True:                     # menu loop
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "":
            continue                # skip empty input, show menu again
        elif choice == "1":
            menu_add_student()
        elif choice == "2":
            menu_view_all()
        elif choice == "3":
            menu_search_student()
        elif choice == "4":
            menu_analytics()
        elif choice == "5":
            menu_ranked_list()
        elif choice == "6":
            print("\nExiting... Thank you for using the analyzer!")
            break                    # break out of the while loop
        else:
            print("Invalid choice. Please select between 1 and 6.")


if __name__ == "__main__":
    main()
