class User(object):
    name = None

    def __init__(self, name):
        self.name = name


    def print_user(self):
        print('The object user name is '+self.name)



class Admin(User):
    def programming(self):
        print("This is admin programming "+self.name)

class Office(User):

   # def __init__(self, name = 'Rex'):
    #    self.name = name


    def programming(self):
        print('This is office programming :'+self.name)