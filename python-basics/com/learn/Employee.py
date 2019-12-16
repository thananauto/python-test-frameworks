class Employee:
    'This is sample class for employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display(self):
        print('The total number of employee count is %d' %Employee.empCount)

    def displayName(self):
        print('Name: ', self.name, ' and the salary is ', self.salary)




