#!/usr/bin/python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names

    def grade_to_points(grade):
        if 94 <= grade <= 100:
            return 4.0
        elif 87 <= grade <= 93:
            return 3.5
        elif 83 <= grade <= 86:
            return 3.0
        elif 76 <= grade <= 82:
            return 2.5
        elif 72 <= grade <= 75:
            return 2.0
        elif 65 <= grade <= 71:
            return 1.5
        elif 61 <= grade <= 64:
            return 1.0
        else:
            return 0.0
        
    def calculate_GPA(self, email, grade, course_name, coursefile, studentfile):
    # Init values
        total_points = 0
        total_credits = 0
    
        for student in studentfile:
            if student['email'] == email:
                for course in student['courses']:
                    if course_name == course['course_name']:
                        temp_grade = grade
                        temp_name = course_name
                    else:
                        continue  # Skip if course name does not match
                
                    # Find corresponding course credit
                    temp_credit = 0
                    for course_info in coursefile:
                        if course_name == course_info['course_name']:
                            temp_credit = course_info['credits']
                            break  # Stop searching once found

                    # Check if course credit was found
                    if temp_credit == 0:
                        print(f"Course '{course_name}' not found in coursefile.")
                        continue

                    print(f"Temp course: {temp_name}")
                    print(f"Temp Grade: {temp_grade}")
                    print(f'Credits: {temp_credit}')
                
                    # Calculate percentage and GPA points
                    percent = (int(temp_grade) / temp_credit) * 100
                    print(f"Percent: {percent}")

                    points = Student.grade_to_points(percent)
                    print(f"Points: {points}")
                
                    total_points += points * temp_credit
                    print(f"Total points: {total_points}")
                    total_credits += temp_credit
                    print(f"Total Credits: {total_credits}")

        # Avoid division by zero
        if total_credits == 0:
            return 0.0

        gpa = total_points  / total_credits
        return gpa