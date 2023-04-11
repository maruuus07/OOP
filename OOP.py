class Student:
    students_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students_list.append(self)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grades(self, grades):
        result = 0
        for course, grade in grades.items():
            result = sum(grade) / len(grade)
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет данных для сравнения')
        if self.avg_grades(self.grades) < other.avg_grades(other.grades):
            return f'Средняя оценка за дз {self.name} {self.surname} < средней оценки за дз {other.name} {other.surname}'
        else:
            return f'Средняя оценка за дз {self.name} {self.surname} > средней оценки за дз {other.name} {other.surname}'

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        course_finished = ', '.join(self.finished_courses)
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grades(self.grades)} ' \
                       f'\nКурсы в процессе изучения: {courses_in_progress}  \nЗавершенные курсы: {course_finished} \n'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lectors_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lectors_list.append(self)

    def avg_grades(self, grades):
        result = 0
        for course, grade in grades.items():
            result += sum(grade) / len(grade)
        return result / len(grades)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет данных для сравнения')
        if self.avg_grades(self.grades) < other.avg_grades(other.grades):
            return f'Средняя оценка за лекции {self.name} {self.surname} < средней оценки за лекции {other.name} {other.surname}'
        else:
            return f'Средняя оценка за лекции {self.name} {self.surname} > средней оценки за лекции {other.name} {other.surname}'

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades(self.grades)}\n'
        return some_lecturer


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return some_reviewer

def student_avg_grade(student_list, course_name):
    for student in student_list:
        if course_name in student.courses_in_progress:
            if course_name in student.grades:
                course_grade_all = []
                avg = sum(student.grades.get(course_name)) / len(student.grades.get(course_name))
                course_grade_all.append(avg)
    all_avg = sum(course_grade_all) / len(course_grade_all)
    return f'Средняя оценка за домашние задания по всем студентам по курсу {course_name} - {all_avg}'

def lecturer_avg_grade(lecturer_list, course_name):
    for lecturer in lecturer_list:
        if course_name in lecturer.courses_attached:
            if course_name in lecturer.grades:
                course_grade_all = []
                avg = sum(lecturer.grades.get(course_name)) / len(lecturer.grades.get(course_name))
                course_grade_all.append(avg)
    all_avg = sum(course_grade_all) / len(course_grade_all)
    return f'Cредняя оценка за лекции всех лекторов по курсу {course_name} - {all_avg}'


student1 = Student('Василий', 'Петров', 'Муж')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Основы программирования']
student2 = Student('Игнат', 'Иванов', 'Муж')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['C++']
lecturer1 = Lecturer('Иван', 'Сорокин')
lecturer1.courses_attached += ['Python']
lecturer2 = Lecturer('Михаил', 'Мишин')
lecturer2.courses_attached += ['Python']
reviewer1 = Reviewer('Ирина', 'Смехова')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Никита', 'Михалков')
reviewer2.courses_attached += ['Python']
student1.rate_hw(lecturer1, 'Python',  8)
student1.rate_hw(lecturer2, 'Python',  9)
student2.rate_hw(lecturer1, 'Python',  10)
student2.rate_hw(lecturer2, 'Python',  10)
reviewer1.rate_hw(student1, 'Python',  5)
reviewer1.rate_hw(student2, 'Python',  3)
reviewer2.rate_hw(student1, 'Python',  9)
reviewer2.rate_hw(student2, 'Python',  6)


print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)
print(student2.__lt__(student1))
print(lecturer1.__lt__(lecturer2))
print()

print(student_avg_grade(Student.students_list, 'Python'))
print(lecturer_avg_grade(Lecturer.lectors_list, 'Python'))

