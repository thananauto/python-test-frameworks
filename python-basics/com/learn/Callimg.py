from com.learn.Employee import Employee
from com.learn.David import David
from com.learn.Cars import Cars


employee1 = Employee('zara', 2000)
employee2 = Employee('Mary', 5000)

employee1.displayName()
employee1.display()
employee2.displayName()
employee2.display()

if hasattr(employee1, 'salary'):
    setattr(employee1, 'salary', 9000)
else:
    setattr(employee1, 'name', 'sukumar')


employee1.displayName()
child = David('lob', 89)
child.displayChildmethod()

child1 = Cars("rupan", 456)
#setattr(child1, 'brandName', 'Audi')
#setattr(child1, 'horsepower', 345)

print(child1.displaycar())

from com.learn.Questions import Questions

question_formats = ["What is the banana color? \n a) blue\n b) black\n c)yellow \n\n"

                    ,"What is the apple color? \n a) red\n b)green\n c)yellow\n\n", "What is the kiwi color?\n a)brown \n b)blue\n c)yellow\n\n"]


questions = [Questions(question_formats[0], "c"), Questions(question_formats[1], "a"), Questions(question_formats[2], "a")]


def test_method(questions):
    score = 0
    for question in questions:
        inputAnswer = input(question.question_prompt)
        if inputAnswer == question.question_answer:
             score += 1
        print("Total score for the test is "+ str(score))


test_method(questions)