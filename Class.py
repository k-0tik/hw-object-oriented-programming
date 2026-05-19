class Student:
    def __init__ (self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'
    def average_score(self):
        grades = []
        for grades_list in self.grades.values():
            grades.extend(grades_list)
        if len(grades) == 0:
            return 0
        return round(sum(grades) / len(grades), 1)
    def __eq__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.average_score() == other.average_score()
        return 'Error'
    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.average_score() < other.average_score()
        return 'Error'
    def __gt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):    
            return self.average_score() > other.average_score()
        return 'Error'
    def __str__(self):
        return (f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средняя оценка за домашние задания:{self.average_score()}\n'
                f'Курсы в процессе изучения:{self.courses_in_progress}\n'
                f'Завершенные курсы:{self.finished_courses}')

class Mentor:
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    

class Lecturer(Mentor):
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def average_score(self):
        grades = []
        for grades_list in self.grades.values():
            grades.extend(grades_list)
        if len(grades) == 0:
            return 0
        return round(sum(grades) / len(grades), 1)
    def __str__(self):
        return (f'Имя:{self.name}\n'
        f'Фамилия:{self.surname}\n'
        f'Средняя оценка за лекции:{self.average_score()}')
    def __eq__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.average_score() == other.average_score()
        return 'Error'
    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.average_score() < other.average_score()
        return 'Error'
    def __gt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):    
            return self.average_score() > other.average_score()
        return 'Error'

class Reviewer(Mentor):
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'
    def __str__(self):
        return (f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}')
    
def overall_gpa_hw(students{}, ):
    return 

def overall_gpa():
    return 

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Антон', 'Антонов')
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Алексей', 'Алексеев')
student_1 = Student('Ольга', 'Алёхина', 'Ж')
student_2 = Student('Олег', 'Алёхин', 'М')
 
student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Python', 'C++']

lecturer_1.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Java', 'C++']

reviewer_1.courses_attached += ['Python', 'C++']
reviewer_2.courses_attached += ['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 4)
 
print(student_1.rate_lecture(lecturer_1, 'Python', 7))    # None
print(student_1.rate_lecture(lecturer_1, 'Java', 8))    # Ошибка
print(student_1.rate_lecture(lecturer_1, 'C++', 8))    # Ошибка
print(student_1.rate_lecture(reviewer_1, 'Python', 6))    # Ошибка

print(student_2.rate_lecture(lecturer_2, 'C++', 8))
print(student_1.rate_lecture(lecturer_2, 'Java', 6))
 
print(lecturer_1.grades)    # {'Python': [7]}
print(lecturer_2.grades)    # {'C++': [8], 'Java': [6]}

print(reviewer_1)
print(lecturer_1)
print(student_1)
print(reviewer_2)
print(lecturer_2)
print(student_2)

print(student_1 < student_2)    # True
print(student_1 > student_2)    # False
print(student_1 == student_2)    # False
print(student_1 < lecturer_2)    # Error

print(lecturer_1 < lecturer_2)    # False
print(lecturer_1 > lecturer_2)    # False
print(lecturer_1 == lecturer_1)    # True
print(lecturer_1 == reviewer_1)    # Error

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']

# cool_mentor = Mentor ('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True

# print(lecturer.courses_attached)    # []
# print(reviewer.courses_attached)    # []

# print(best_student.grades)