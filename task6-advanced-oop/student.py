from typing import List

class Student:
    def __init__(self, name: str, age: int, student_id: str) -> None:
        self.name = name
        self.age = age
        self.student_id = student_id
        self._courses: List['Course'] = []  # Track the courses the student is enrolled in

    def enroll_in_course(self, course: 'Course') -> None:
        """Enroll a student in a course."""
        self._courses.append(course)

    def __repr__(self) -> str:
        return f"Student(name={self.name}, age={self.age}, student_id={self.student_id})"

    def __iter__(self):
        return iter(self._courses)  # Allows iteration over enrolled courses
