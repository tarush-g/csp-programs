import random

class Student:
    def __init__(self, name):
        self.name = name
        self.idNumber = random.randint(10000000, 99999999)

    def __str__(self):
        return "student: " + self.name +" id: " + str(self.idNumber)
    
    def setGradeLevel(self, gradeLevel):
        self.gradeLevel = gradeLevel

    def speak(self, message):
        print(message)

x = list()
student1 = Student("Frank")
student1.setGradeLevel(12)
print(student1)
print(student1.gradeLevel)
