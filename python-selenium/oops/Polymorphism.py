class Polymorphism(object):
    def __init__(self, name):
        self.name=name
# this is example for abstract class as well
    def show(self):
        raise NotImplementedError('Sub class must implement abstract method')

class PDF(Polymorphism):

    def show(self):
        return "Show the contents "+self.name

class WORD(Polymorphism):

    def show(self):
        return "Show the contents " + self.name

class XML(Polymorphism):

    def show(self):
        return "Show the contents "+self.name

if __name__ == '__main__':
    files = [PDF('payslip'), WORD('Data'), XML('Valigan')]

    for file in files:
        print('Document name :'+file.name+' Contents :'+file.show())