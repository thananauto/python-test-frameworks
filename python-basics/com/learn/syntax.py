#if-else condition check
if True:
    print('true')
elif False:
    print('false')


# multi line statement
first = 'first'; second = 'second'; third = 'third'

total = first + \
        second + \
        third
print (total)

#multi statement in single line
import sys; x = 'foo'; sys.stdout.write(x+'\n')

# assign variables
a= b = c =1
x,y,z = 1,2,'literals'

print(z[2:])
print(z*2)

# python lists
list = ['abcd', 786, "Man hover", 70.2, 8]
print(list[2:5])

# math statement
import math

print(math.ceil(9))

if cmp(3,4) == 1:
    print('3 less than 4')
else :
    print('4 less than 3')