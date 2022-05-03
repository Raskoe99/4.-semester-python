# python_students.py

class PythonStudents:
    
    def __init__(self):
        self.students = []

    def __add__(self, student):
        self.students.append(student)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        ri = self.index
        self.index += 1
        if self.index > len(self.students):
            raise StopIteration()
        return self.students[ri]



class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
            return self.__name

    @name.setter
    def name(self, name):
            self.__name = name.capitalize()

    def __add__(self, student):
            return Student('Anna the daugther', 1234)

    def __str__(self):
            return f'{self.name}, {self.cpr}'

    def __repr__(self):
            return f'{self.__dict__}'


studentList = PythonStudents()
student1 = Student("Khadeja", 69)
student2 = Student("Rasmus", 420)

studentList + student1
studentList + student2

for i in studentList:
    print(i.name)


