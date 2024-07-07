# -*- coding: utf-8 -*-
"""Python__OOP.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Ducanhngo/AIO_2024_087_AnhDuc/blob/feature%2Fexercise/Python__OOP.py

#Question 1
"""

import torch
import torch.nn as nn
data = torch.Tensor([1,2,3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)

"""#Question 2"""

import torch
import torch.nn as nn

class My_Softmax(nn.Module):
  def __init__(self):
    super().__init__()
  def forward(self, x):
    return torch.exp(x)/torch.sum(torch.exp(x))
data = torch.Tensor([5 , 2 , 4])
my_softmax = My_Softmax()
output = my_softmax(data)
print(output)

"""#Question 3

"""

import torch
import torch.nn as nn

class My_Softmax(nn.Module):
  def __init__(self):
    super().__init__()
  def forward(self, x):
    return torch.exp(x)/torch.sum(torch.exp(x))
data = torch.Tensor([1, 2, 300000000])
my_softmax = My_Softmax()
output = my_softmax(data)
print(output)

"""#Question 4"""

import torch
import torch.nn as nn

class Softmax_Stable(nn.Module):
  def __init__(self):
    super().__init__()
  def forward(self, x):
    x_max = torch.max(x, dim = 0, keepdims = True)
    x_exp = torch.exp(x - x_max.values)
    partition = x_exp.sum(0, keepdim = True)
    return x_exp/partition
data = torch.Tensor([1,2,3])
my_softmax = Softmax_Stable()
output = my_softmax(data)
print(output)

"""#Question 5:"""

from abc import ABC, abstractmethod

class Person(ABC):
  def __init__(self, name: str, yob: int):
    self._name = name
    self._yob = yob
    def get_yob(self):
      return self._yob
    @abstractmethod
    def describe(self):
      pass
class Student(Person):
  def __init__(self,name: str, yob: int, grade: str):
    self._name = name
    self._yob = yob
    self._grade = grade
  def describe(self):
    print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

student1 = Student(name ="studentZ2023", yob =2011 , grade ="6")
student1.describe()

"""
#Question 6:
"""

from abc import ABC, abstractmethod

class Person(ABC):
  def __init__(self, name: str, yob: int):
    self._name = name
    self._yob = yob
    def get_yob(self):
      return self._yob
class Teacher(Person):
  def __init__(self,name: str, yob: int, subject: str):
    self._name = name
    self._yob = yob
    self._subject = subject
  def describe(self):
    print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

teacher1 = Teacher(name ="teacherZ2023", yob =1991 , subject ="History")
teacher1.describe()

"""#Question 7"""

from abc import ABC, abstractmethod

class Person(ABC):
  def __init__(self, name: str, yob: int):
    self._name = name
    self._yob = yob
    def get_yob(self):
      return self._yob
class Doctor(Person):
  def __init__(self,name: str, yob: int, specialist: str):
    self._name = name
    self._yob = yob
    self._specialist = specialist
  def describe(self):
    print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")

doctor1 = Doctor ( name ="doctorZ2023", yob =1981 , specialist ="Endocrinologists")
doctor1.describe()

"""#Question 8"""

class Person:
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    def describe(self):
        print(f"Name: {self.name}, YoB: {self.yob}")

class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student Name: {self.name}, YoB: {self.yob}, Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher Name: {self.name}, YoB: {self.yob}, Subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor Name: {self.name}, YoB: {self.yob}, Specialist: {self.specialist}")

class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__listPeople = list()

    def add_person(self, person: Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listPeople:
            p.describe()

    def count_doctor(self):
        return sum(1 for person in self.__listPeople if isinstance(person, Doctor))

student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

print(ward1.count_doctor())

"""#Question 9"""

class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if not self.is_full():
            self.__stack.append(value)

stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.is_full())

"""#Question 10"""

class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if not self.is_full():
            self.__stack.append(value)

    def top(self):
        if self.__stack:
            return self.__stack[-1]

stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.top())

"""#Question 11"""

class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if not self.is_full():
            self.__queue.append(value)

queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.is_full())

"""#Question 12"""

class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def isEmpty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if not self.is_full():
            self.__queue.append(value)

    def front(self):
        if not self.isEmpty():
            return self.__queue[0]

queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.front())
