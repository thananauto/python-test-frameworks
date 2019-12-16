# calling the function within the function
def lower(text):
    return text.lower()

def upper(text):
    return text.upper()

def parent_function(func):
    greeting = func(" This is the sample letter")
    print(greeting)

parent_function(lower)
parent_function(upper)

# function return the another function

def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(10)

print(add_15(20))

