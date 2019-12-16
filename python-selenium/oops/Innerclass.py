class Innerclass(object):


    def __init__(self):
        self.head = Head()
        self.foot = Foot()

    def health(self):
        print('My health is good')

class Head:

    def activity(self):
        print('Head start thinking')



class Foot:

    def activity(self):
        print("My foot have two legs")


if __name__ == '__main__':

    innerclass = Innerclass()
    innerclass.foot.activity()
    innerclass.head.activity()
    innerclass.health()
