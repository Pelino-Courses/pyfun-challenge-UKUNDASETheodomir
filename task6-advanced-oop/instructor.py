from __future__ import annotations  
from person import Person
from typing import List

class Instructor(Person):
    def __init__(self, name: str, age: int, employee_id: str) -> None:
        super().__init__(name, age)
        self.employee_id = employee_id
        self._courses: List[Course] = []  

    def assign_course(self, course: Course) -> None:
        from course import Course 

        if not isinstance(course, Course):
            raise TypeError("Expected a Course instance.")

        if course not in self._courses:
            self._courses.append(course)
            course.assign_instructor(self)

    def __repr__(self) -> str:
        return f"Instructor(name={self.name}, age={self.age}, id={self.employee_id})"
