import sys
from grade_book import GradeBook
def exit_app():
    print("Thanks for using the Grade Book App!")
    print("Goodbye!")
    sys.exit()

def main():
    student_file = "students.json"
    course_file = "courses.json"
    gradebook = GradeBook(student_file, course_file)
    while True:
        print("\nChoose an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            gradebook.add_student()
        elif choice == '2':
            gradebook.add_course()
        elif choice == '3':
            gradebook.register_student_for_course()
        elif choice == '4':
            gradebook.calculate_ranking()
        elif choice == '5':
            gradebook.search_by_grade()
        elif choice == '6':
            gradebook.generate_transcript()
        elif choice == '7':
            exit_app()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()