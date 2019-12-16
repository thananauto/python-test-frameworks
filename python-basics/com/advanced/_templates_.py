from string import Template

class TemplateExample(Template):
    delimiter = '#'

    def template_example(self):
        data_set =[dict(fruitName="Orange", price = 6, count = 5), dict(fruitName= "grapes", price = 8, count = 7), dict(fruitName = "Pomo", price = 15, count = 9)]
        temp = Template("#fruitName x #count = #price")
        total= 0
        for data in data_set:
            print(temp.substitute(data))
            total += data["price"]
        print("The total amount of fruit is "+str(total))



if __name__=="__main__":

    t = TemplateExample(Template)
    t.template_example()