class Encapsulation(object):
    # the variable or methods starts with '__' is private keywords
    __name = None
    __speed = None
    __brand = None

    def set_name(self, name):
        self.__name = name

    def set_speed(self, speed):
        self.__speed = speed

    def set_brand(self, brand):
         self.__brand = brand

    def print_product(self):
         print('The name of the car is '+self.__brand+' and it has the speed of '+str(self.__speed)+' and the owner name is '+self.__name)

    def print_name(self):
        if not(not self.__name):
            print('The name has some values')
        else:
            print('The name does not have any values')

    # this is the private method and it can't be called outside the class's
    def __print_name_none(self):
        if self.__name is None:
            print('The name has some values')
        else:
            print('The name does not ghave any values')

    def method_overloading(self, name=None):
        if name is not None:
            print('Hello... ' + name)
        else:
            print("Hello Mr!...")

