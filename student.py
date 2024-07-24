#!/usr/bin/python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names

    def grade_to_points(grade):
        if 90 <= grade <= 100:
            return 4.0
        elif 80 <= grade <= 89:
            return 3.0
        elif 70 <= grade <= 79:
            return 2.0
        elif 60 <= grade <= 69:
            return 1.0
        else:
            return 0.0
    
    def calculate_GPA(self, grade, courses, studentfile, cour_name):
        total_points = 0
        total_credits = 0

        for course in courses:
            course_name = course['course_name']
            print(f'{course_name}')
            credits = int(course['credits'])
            print(f'Credits: {credits}')
            if course_name in studentfile:
                temp_grade = studentfile[course_name]
            elif course_name == cour_name:
                temp_grade = grade
            else:
                temp_grade = 0
            percent = (int(temp_grade) / credits) * 100
            print(f"Percent:{percent}")

            points = Student.grade_to_points(percent)
            print(f"Points: {points}")
            total_points += points * credits
            print(f"Total points: {total_points}")
            if not total_points == 0:
                total_credits += credits
            print(f"Pending Credits: {total_credits}")    
        if total_credits == 0:
            return 0.0
        print(f"Total Credits: {total_credits}")
        gpa = total_points / total_credits
        return gpa