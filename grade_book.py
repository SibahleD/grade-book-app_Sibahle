#!/usr/bin/python3
import os
import json
from student import Student
from course import Course
class GradeBook:
    def __init__(self, student_file, course_file, reg_course_file):
        self.student_file = student_file
        self.course_file = course_file
        self.reg_course_file = reg_course_file        
        for file in [student_file, course_file, reg_course_file]:
            if not os.path.exists(file):
                open(file, "w").close()
        
    def loadjson(self, filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def savejson(self, my_obj, filename):
        with open(filename, 'w') as f:
            json.dump(my_obj, f, indent=4)

    def add_student(self):
        # Email validation
        new_email = input("Enter student's email: ")
        if "@" not in new_email or "." not in new_email:
            print("Invalid email format (must contain '@' and '.')")
            print("Student not added successfully")
            return
        
        # Name validation
        new_names = input("Enter student's names: ")
        if len(new_names) == 0:
            print("Student names cannot be empty")
            print("Student not added successfully")
            return
        
        # Check if email already exists
        students = self.loadjson(self.student_file)

        for student in students:
            if student.get('email') == new_email:
                print("Email already exists")
                print("Student not added successfully")
                return
        
        # Initializing new info
        new_student = Student(new_email, new_names).__dict__  

        # Append new Student info
        students.append(new_student)
        
        # Saving into json file
        self.savejson(students, self.student_file)
        print("New student added successfully!")

    def add_course(self):
        # Name validation
        new_course_name = input("Enter course name: ")
        if len(new_course_name) == 0:
            print("Course name cannot be empty")
            print("Course not added successfully")
            return
        
        trimester = input("Enter trimester: ")
        # Credits validation
        try:
            credits = int(input("Enter course credits: "))
        except ValueError:
            print("Credits should be digits")
            print("Course not added successfully")
            return
        # Check if course already exists
        courses = self.loadjson(self.course_file)
        for c in courses:
            if c.get('course_name') == new_course_name:
                print("Course already exists")
                print("Course not added successfully")
                return
        # Initializing and appending new info
        new_course = Course(new_course_name, trimester, credits).__dict__
        courses.append(new_course)
        
        # Saving into json file
        self.savejson(courses, self.course_file)
        print("New course added successfully!")
    
    def register_student_for_course(self):

        # Email validation
        student_email = input("Enter student's email: ")
        if "@" not in student_email or "." not in student_email:
            print("Invalid email format (must contain '@' and '.')")
            print("Student not added successfully")
            return

        students = self.loadjson(self.student_file)
        student = None
        for e in students:
            if e.get('email') == student_email:
                student = e
                break
    
        if student is None:
            print("Email does not exist")
            return

        # Course validation  
        course_name = input("Enter course name: ")
        courses = self.loadjson(self.course_file)
        course = None
        for c in courses:
            if c.get('course_name') == course_name:
                course = c
                break
    
        if course is None:
            print("Course does not exist")
            return

        grade = input("Enter grade: ")

        # Adding record to file
        student_courses = student.get('courses', [])
        student_courses.append({"course_name": course_name, "grade": grade})
        student['courses'] = student_courses
    
        self.savejson(students, self.student_file)
        print("Student registered successfully!")

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
