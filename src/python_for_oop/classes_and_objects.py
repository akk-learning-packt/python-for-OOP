#!/usr/bin/env python3


class Student:
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = name
        self.marks = marks

    def result(self):
        if self.marks > 500:
            return "Pass"
        else:
            return "Fail"


Student1 = Student("Arun", 1234, 500)
print(Student1.name)
print(Student1.result())

Student2 = Student("Hitler", 764, 600)
print(Student2.marks)
print(Student2.result())
