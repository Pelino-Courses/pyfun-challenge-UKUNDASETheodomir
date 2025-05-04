from student import Student  # Import Student class
from instructor import Instructor  # Import Instructor class

class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str, age: int, student_id: str, instructor_id: str) -> None:
        # Initialize both Student and Instructor attributes
        Student.__init__(self, name, age, student_id)  # Initialize Student part
        Instructor.__init__(self, name, age, instructor_id)  # Initialize Instructor part

    def __repr__(self) -> str:
        return f"TeachingAssistant(name={self.name}, age={self.age}, student_id={self.student_id}, instructor_id={self.instructor_id})"
