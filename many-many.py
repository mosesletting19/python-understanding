class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)

class Course:
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        
# Create students
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Create courses
course1 = Course("Python Fundamentals", "John Smith")
course2 = Course("Web Development", "Jane Doe")

# Establish the many-to-many relationship
student1.enroll_course(course1)
student1.enroll_course(course2)
student2.enroll_course(course1)

# Accessing courses for a specific student
print(f"Courses enrolled by {student1.name}:")
for course in student1.courses:
    print(course.name)

# Accessing students enrolled in a specific course
print(f"Students enrolled in {course1.name}:")
for student in course1.students:
    print(student.name)