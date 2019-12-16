import logging as log
class HelloWord:
    z=10

    def print_Hello_world(self):
        print("This is sample hello world example")
        log.debug("This is debug message")


    def string_comparison(self, fs):
        if fs.lower()== "firSt String".lower():
            print("Bothe string are equal")
        else:
            print("Both string are not equal")

    def string_index(self, string, start_index, end_index):
        if (start_index == "") or ( start_index == 0):
            print(string[end_index:])
        elif (not end_index) and (not start_index):
            print(string[start_index:end_index])

    def sort_array(self, array):
        print(array.sort())
        print(array)



    def local_and_global_variable(self):
        global z
        self.z = 0
        print(self.z)

    def cube_number(self, cube_number):
        return cube_number*cube_number*cube_number


    def func_inside_function(self, z):
        return z * self.cube_number(z)

    def factorial(self, number):
        if number == 1:
            return 1
        else:
            log.debug("Its in recurssive function and the value of N is "+str(number))
            return number * self.factorial(number - 1)

print(__name__)

if __name__ == '__main__':
     log.basicConfig(format='%(asctime)s %(message)s', level=log.DEBUG)
     hellowWorld = HelloWord()
     hellowWorld.print_Hello_world()
     hellowWorld.string_comparison("first String")
     hellowWorld.string_index("first string", "", 3)

     sort_array = ["four", 'yummy', 'True', "felix"]
     hellowWorld.sort_array(sort_array)
    # hellowWorld.z = 9
     hellowWorld.local_and_global_variable()
     print("The factorial value is "+ str(hellowWorld.factorial(7)))
     print("The global variable is ", hellowWorld.z)

     print(hellowWorld.cube_number(5))

     print(hellowWorld.func_inside_function(2))
