#!/usr/bin/python3
from student import Student
class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
    
    def add_student(self):
        new_email = input("Enter student's email: ")
        # Email validation
        if "@" not in new_email or "." not in new_email:
            print("Invalid email format('@' should be present)")
            print("Student not added succesfully")
            return
        new_names = input("Enter student's names: ")
        if len(new_names) == 0:
            print("Student names cannot be empty")
            print("Student not added succesfully")
            return
        new_student = Student(new_email, new_names)
        self.student_list.append(new_student)
        print("New student added succesfully!")
    
    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter trimester: ")
        credits = int(input("Enter course credits: "))
        course = course(name, trimester, credits)
        self.course_list.append(course)
    
    def register_student_for_course(self):
        student_email = input("Enter student's email: ")
        course_name = input("Enter course name: ")
        grade = input("Enter grade: ")
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
    
    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda student: student.GPA, reverse=True)
    
    def search_by_grade(self, course_name, grade):
        students_with_grade = []
        for student in self.student_list:
            for course in student.courses_registered:
                if course['course'].name == course_name and course['grade'] == grade:
                    students_with_grade.append(student)
        return students_with_grade
    
    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if not student:
            return None
        transcript = {
            'email': student.email,
            'names': student.names,
            'courses': [(c['course'].name, c['grade']) for c in student.courses_registered],
            'GPA': student.GPA
        }
        return transcript
