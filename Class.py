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
        return f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.average_score()}'

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
        return f'Имя:{self.name}\nФамилия:{self.surname}'

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алёхина', 'Ж')
 
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'C++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 
print(lecturer.grades)  # {'Python': [7]}

print(reviewer)
print(lecturer)
print(student)

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