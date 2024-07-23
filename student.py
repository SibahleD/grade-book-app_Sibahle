#!/usr/bin/python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def to_dict(self):
        """Convert the Student object to a dictionary."""
        return {
            'email': self.email,
            'names': self.names,
            'courses_registered': self.courses_registered,
            'GPA': self.GPA
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary."""
        student = cls(data['email'], data['names'])
        student.courses_registered = data.get('courses_registered', [])
        student.GPA = data.get('GPA', 0.0)
        return student
    
    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
        else:
            total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
            total_credits = sum(course['credits'] for course in self.courses_registered)
            self.GPA = total_points / total_credits if total_credits > 0 else 0.0
    
    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})
        self.calculate_GPA()