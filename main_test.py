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
            ranking = GradeBook.calculate_ranking()
            for idx, student in enumerate(ranking, start=1):
                print(f"{idx}. {student.names} (GPA: {student.GPA:.2f})")
        elif choice == '5':
            students = gradebook.search_by_grade()
            for student in students:
                print(f"{student.names} ({student.email})")
        elif choice == '6':
            email = input("Enter student's email: ")
            transcript = gradebook.generate_transcript(email)
            if transcript:
                print(f"Transcript for {transcript['names']} ({transcript['email']}):")
                for course_name, grade in transcript['courses']:
                    print(f"{course_name}: {grade}")
                print(f"GPA: {transcript['GPA']:.2f}")
            else:
                print("Student not found.")
        elif choice == '7':
            exit_app()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()