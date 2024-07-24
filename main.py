#!/usr/bin/python3
import sys
from course import course
from grade_book import grade_book
from student import students

def exit_app():
    print("Thanks for using the Grade Book App!")
    print("Goodbye!")
    sys.exit()

def main():
    while True:
        print("\nWelcome to the Grade Book App!")
        print("Please select an option:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student to course")
        print("4. Calculate ranking")
        print("5. Search by grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":

            grade_book.add_student()
        elif choice == "2":
            add_course() # type: ignore
        elif choice == "3":
            register_student_for_course() # type: ignore
        elif choice == "4":
            calculate_ranking() # type: ignore
        elif choice == "5":
            search_by_grade() # type: ignore
        elif choice == "6":
            students.generate_transcript()
        elif choice == "8":
            exit_app()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
