from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

def main():
    # Create instances
    course1 = Course("CS101", "Introduction to Computer Science", 30)
    course2 = Course("MATH101", "Calculus I", 25)

    student1 = Student("Theo", 20, "S12345")
    student2 = Student("MUGABO", 21, "S67890")
    
    instructor1 = Instructor("Dr. TWAGIRAYEZU Evariste", 45, "I001")
    ta1 = TeachingAssistant("Charlie", 22, "S11223", "I002")

    # Enroll students
    enrollment = Enrollment()
    enrollment.enroll(student1, course1)
    enrollment.enroll(student2, course1)
    enrollment.enroll(student1, course2)
    enrollment.enroll(ta1, course1)

    # Assign instructor
    course1.assign_instructor(instructor1)

    # Display information
    print(f"Courses for {student1.name}: {[course.title for course in student1]}")
    print(f"Students in {course1.title}: {[student.name for student in course1]}")
    print(f"Instructor for {course1.title}: {course1._instructor.name}")
    print(f"Teaching Assistant: {ta1.name}")

if __name__ == "__main__":
    main()
