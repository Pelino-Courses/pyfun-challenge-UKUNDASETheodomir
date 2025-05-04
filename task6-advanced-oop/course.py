from typing import List

class Course:
    def __init__(self, code: str, title: str, capacity: int) -> None:
        self.code = code
        self.title = title
        self.capacity = capacity
        self._students: List['Student'] = []  # List of students enrolled in the course
        self._instructor = None

    def add_student(self, student: 'Student') -> None:
        """Add a student to the course if there's room."""
        if len(self._students) < self.capacity and student not in self._students:
            self._students.append(student)

    def assign_instructor(self, instructor: 'Instructor') -> None:
        """Assign an instructor to the course."""
        self._instructor = instructor

    def __repr__(self) -> str:
        return f"Course(code={self.code}, title={self.title}, capacity={self.capacity})"

    def __iter__(self):
        return iter(self._students)
