class Car(object):

    def create_object(type):
        if type == 'audi':
            return Audi()
        elif type == 'benz':
            return Benz()

    factory = staticmethod(create_object)

class Audi(Car):

    def display(self):
        print('Audi is good car')

class Benz(Car):

    def display(self):
        print('Benz is good car')



if __name__ == '__main__':

    car = Car.factory('audi')
    car.display()

    car = Car.factory('benz')
    car.display()