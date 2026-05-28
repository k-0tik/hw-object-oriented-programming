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
        if grade < 1 or grade > 10:
            return 'Оценка может быть числом от 1 до 10'
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Вы пытаетесь поставить оценку лектору, который не преподает на этом курсе или не является преподавателем'
    def average_score(self):
        grades = []
        for grades_list in self.grades.values():
            grades.extend(grades_list)
        if len(grades) == 0:
            return 0
        return round(sum(grades) / len(grades), 1)
    def course_average_score(self, course):
        if course in self.courses_in_progress or course in self.finished_courses:
            if course in self.grades and len(self.grades[course]) > 0:
                return round(sum(self.grades[course]) / len(self.grades[course]), 1)
            else:
                return 'У студента нет оценок'
        return 'Студент не учится на этом курсе'
    def __eq__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.average_score() == other.average_score()
        return 'Вы пытаетесь сравнивать представителей разного класса'
    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.average_score() < other.average_score()
        return 'Вы пытаетесь сравнивать представителей разного класса'
    def __gt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):    
            return self.average_score() > other.average_score()
        return 'Вы пытаетесь сравнивать представителей разного класса'
    def __str__(self):
        return (f'\n'
                f'Имя:{self.name}\n'
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
        super().__init__ (name, surname)
        self.courses_attached = []
        self.grades = {}
    def average_score(self):
        grades = []
        for grades_list in self.grades.values():
            grades.extend(grades_list)
        if len(grades) == 0:
            return 0
        return round(sum(grades) / len(grades), 1)
    def course_average_score(self, course):
        if course in self.courses_attached:
            return round(sum(self.grades[course]) / len(self.grades[course]), 1)
        return 'У преподавателя нет оценок или он не преподает на этом курсе'
    def __str__(self):
        return (f'\n'
                f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средняя оценка за лекции:{self.average_score()}')
    def __eq__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.average_score() == other.average_score()
        return 'Вы пытаетесь сравнивать представителей разного класса'
    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.average_score() < other.average_score()
        return 'Вы пытаетесь сравнивать представителей разного класса'
    def __gt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):    
            return self.average_score() > other.average_score()
        return 'Вы пытаетесь сравнивать представителей разного класса'

class Reviewer(Mentor):
    def __init__ (self, name, surname):
        super().__init__ (name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if grade < 1 or grade > 10:
            return 'Оценка может быть числом от 1 до 10'
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Вы пытаетесь поставить оценку студенту, котрый не учиться на этом курсе или не является студентом'
    def __str__(self):
        return (f'\n'
                f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}')

    
def overall_gpa_hw(students: list[Student], course: str):
    sum_grade = 0
    count = 0
    for student in students:
        if not isinstance(student, Student) and (course not in student.finished_courses or course not in student.courses_in_progress):
            return f'Студент {student.name} {student.surname} не учится на курсе {course} или не является студентом'
        else:
            if isinstance(student.course_average_score(course), str):
                return f'У студента {student.name} {student.surname} нет оценок по курсу {course}'
            count += 1
            sum_grade += student.course_average_score(course)
    return round(sum_grade / count, 1)

def overall_gpa(lecturers: list[Lecturer], course: str):
    sum_grade = 0
    count = 0
    for lecturer in lecturers:
        if not isinstance(lecturer, Lecturer) and (course not in lecturer.courses_attached):
            return f'Преподаватель {lecturer.name} {lecturer.surname} не преподает на курсе {course} или не является лектором'
        else:
            if isinstance(lecturer.course_average_score(course), str):
                return f'У преподавателя {lecturer.name} {lecturer.surname} нет оценок по курсу {course}'
            count += 1
            sum_grade += lecturer.course_average_score(course)
    return round(sum_grade / count, 1)

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
reviewer_2.rate_hw(student_2, 'Python', 23)    # Error
 
print(student_1.rate_lecture(lecturer_1, 'Python', 7))    # None
print(student_2.rate_lecture(lecturer_1, 'C++', 7))    # None
print(student_1.rate_lecture(lecturer_1, 'Java', 8))    # Error
print(student_1.rate_lecture(lecturer_1, 'C++', 8))    # Error
print(student_1.rate_lecture(reviewer_1, 'Python', 6))    # Error
print(student_2.rate_lecture(lecturer_1, 'C++', 11))    # Error

print(student_2.rate_lecture(lecturer_2, 'C++', 8))    # None
print(student_1.rate_lecture(lecturer_2, 'Java', 6))    # None
 
print(lecturer_1.grades)    # {'Python': [7], 'C++': [7]}
print(lecturer_2.grades)    # {'C++': [8], 'Java': [6]}

print('\n', '--Эксперты--')
print(reviewer_1)
print(reviewer_2)
print('\n', '--Лекторы--')
print(lecturer_1)
print(lecturer_2)
print('\n', '--Студенты--')
print(student_1)
print(student_2)

print('\n', '--Сравнение студентов по среднему баллу--')
print(student_1 < student_2)    # False
print(student_1 > student_2)    # True
print(student_1 == student_2)    # False
print(student_1 < lecturer_2)    # Error

print('\n', '--Сравнение лекторов по среднему баллу--')
print(lecturer_1 < lecturer_2)    # False
print(lecturer_1 > lecturer_2)    # False
print(lecturer_1 == lecturer_2)    # True
print(lecturer_1 == reviewer_1)    # Error

print('\n', '--Общий средний балл за домашние задания по курсу--')
print (overall_gpa_hw([student_1, student_2], 'Python'))    # 6.0
print (overall_gpa_hw([student_1, student_2], 'Java'))    # Error
print (overall_gpa_hw([student_1, student_2], 'C#'))    # Error

print('\n', '--Общий средний балл за лекции по курсу--')
print (overall_gpa([lecturer_1, lecturer_2], 'C++'))    # 7.5
print (overall_gpa([lecturer_1, lecturer_2], 'Java'))    # Error
print (overall_gpa([lecturer_1, lecturer_2], 'C#'))    # Error