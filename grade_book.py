#!/usr/bin/python3
import os
import json
from student import Student
from course import Course
class GradeBook:
    def __init__(self, student_file, course_file):
        self.student_file = student_file
        self.course_file = course_file       
        for file in [student_file, course_file]:
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
    
        # Initializing variable to hold all data
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
        studentfile = self.loadjson(self.student_file)
        student = None
        for e in studentfile:
            if e.get('email') == student_email:
                student = e
                break
        if student is None:
            print("Email does not exist")
            return

        # Course validation  
        course_name = input("Enter course name: ")
        coursefile = self.loadjson(self.course_file)
        course = None
        for c in coursefile:
            if c.get('course_name') == course_name:
                course = c
                break
        if course is None:
            print("Course does not exist")
            return

        grade = int(input("Enter grade: "))

        # Adding record to file
        student_courses = student.get('courses', [])
        student_courses.append({"course_name": course_name, "grade": grade})
        student['courses'] = student_courses
        gpa = Student.calculate_GPA(self, student_email, grade, course_name, coursefile, studentfile)
        print(f"Your GPA is: {gpa:.2f}")
        student['GPA'] = round(gpa, 2)

        self.savejson(studentfile, self.student_file)
        print("Student registered successfully!")
 
    def calculate_ranking(self):
        students = self.loadjson(self.student_file)
        # Sort students by GPA in descending order
        sorted_students = sorted(students, key=lambda x: x['GPA'], reverse=True)
    
         # Initialize rank
        rank = 1
        previous_gpa = None
        previous_rank = None
        for i, student in enumerate(sorted_students):
            if student['GPA'] != previous_gpa:
               student['rank'] = rank
            else:
                student['rank'] = previous_rank
            previous_gpa = student['GPA']
            previous_rank = student['rank']
            rank += 1

        print("Rankings of Students:")
        print("{:<5} {:<20} {:<5} {:<5}".format("Rank", "Name", "GPA", ""))
        
        for student in sorted_students:
            print("{:<5} {:<20} {:<5}".format(student['rank'], student['names'], student['GPA']))

    def search_by_grade(self):
        students = self.loadjson(self.student_file)
    
        course_name = input("Enter course name: ")
        grade = float(input("Enter grade: "))
    
        search_result = []
    
        for student in students:
            for course in student['courses']:
                if course['course_name'] == course_name and course['grade'] == grade:
                    search_result.append(student)
    
        # Return a list of students with the specified grade in the specified course
        
        if not search_result:
            print('No record found')
        
        print("Students in {} with grade {}:".format(course_name, grade))
        index = 0
        for student in search_result:
            index += 1
            print("{}: {}".format(index, student['names']))
            for course in student['courses']:
                if course['course_name'] == course_name and course['grade'] == grade:
                    print("  Course: {} \n  Grade: {}".format(course['course_name'], course['grade']))

    def generate_transcript(self):
        email = input("Enter student's email: ")
        tran_students = self.loadjson(self.student_file)
    
        search_result = []
    
        for student in tran_students:
            if student['email'] == email:
                search_result.append(student)
    
        if not search_result:
            print('No record found')
        else:
            # Assuming there's only one student with that email
            student = search_result[0]
            print("Name: {}".format(student['names']))
            print("GPA: {}".format(student['GPA']))
            for course in student['courses']:
                print("  Course: {} \n  Grade: {}".format(course['course_name'], course['grade']))
                print("")
