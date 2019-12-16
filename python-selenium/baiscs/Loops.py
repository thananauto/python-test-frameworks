from datetime import datetime, timedelta
from random import *
class Loops:

    def for_loop(self, items):
       for item in items:
           print(item)

    def print_millisecond_in_range(self, x, y):
        for i in range(x,y):
            print('The value is range %s is correct'% str(i))

    def print_date_bet_range(self, startDate, endDate):
        currentDate = datetime.now()
        for date in range(startDate, endDate):
             print((currentDate +timedelta(date)).strftime("%a, %b %d, %Y"))


    def guess_number_while(self, correctNumber):
        guess = 0
        while guess != correctNumber:
            guess = int(input("Guess the number: "))
            if(guess!=correctNumber):
               print("You guessed the wrong number")
        print( "Hurray....! you found the correct number")

    def print_odd_numbers(self, numbers):
        for i in numbers:
            print(i)

    def print_even_numbers(self, numbers):
         for i in range(len(numbers)):
             print(numbers[i])

    def tuple_test(self, data):
        for i in range(len(data)):
            print(data[i])

    def dict_test(self, data):
        dict_value = {}
        dict_value['name'] = 'thanan'
        dict_value['Age'] = 50
        dict_value['postcode'] = 3732
        dict_value['city'] = "Chennai"
        print(dict_value)

 

if __name__ == '__main__':
    loops = Loops()
    items = ['mango', 'apple', 'bananan', 'icecream']
    print(loops.for_loop(items))
  # loops.print_millisecond_in_range(3,9)
  # loops.print_date_bet_range(1, 10)
   # loops.guess_number_while(7)

    numbers = list(range(0,20,3))
    #loops.print_odd_numbers(numbers)

    numbers = list(range(0, 20, 2))
    #loops.print_even_numbers(numbers)
    name, age, country = ("thanan", 40, "India");
    loops.tuple_test(country)
    loops.dict_test("")
