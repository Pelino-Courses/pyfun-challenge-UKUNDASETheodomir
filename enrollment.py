from typing import List, Optional, Tuple
from student import Student
from course import Course

class Enrollment:
    """Handles enrollment relationships between students and courses."""

    def __init__(self) -> None:
        self._records: List[Tuple[Student, Course]] = []

    def enroll(self, student: Student, course: Course) -> None:
        """Enroll a student in a course, avoiding duplicate enrollments."""
        if (student, course) in self._records:
            print(f"{student.name} is already enrolled in {course.title}.")
            return

        try:
            student.enroll(course)
            self._records.append((student, course))
        except Exception as e:
            print(f"Enrollment failed: {e}")

    def get_courses_for_student(self, student: Student) -> List[Course]:
        """Return a list of courses that the student is enrolled in."""
        return [course for s, course in self._records if s == student]

    def get_students_in_course(self, course: Course) -> List[Student]:
        """Return a list of students enrolled in a given course."""
        return [student for student, c in self._records if c == course]

    def __repr__(self) -> str:
        return f"Enrollment(records={len(self._records)})"

