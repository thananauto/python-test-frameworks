class Cars:
    'This is the sample class to know more details about car'


    def __init__(self, brandName, horsepower):
        self.brandName = brandName
        self.horsepower = horsepower

    def displaycar(self):
        print('The car brand name'+self.brandName)

    def displayPower(self):
         print('The total horse power is %s' %self.horsepower)


