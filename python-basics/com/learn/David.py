from com.learn.Employee import Employee
from com.learn.Cars import Cars

class David(Employee, Cars):
  def __init__(self, name , salary):
      print('Calling the constrcutor')

  def displayChildmethod(self):
      print('Print calling the child methods')