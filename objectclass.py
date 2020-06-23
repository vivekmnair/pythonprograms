class person:
    def __init__(self,name,age,address):
        self.name=name 
        self.age=age
        self.address=address
    def myfunc(self):
        print("hello my name is " +self.name)
        print("hello my age is " +str(self.age))

p1=person("ABC",35,"THRISSUR")
p1.myfunc()

class proglang:
    def __init__(self,name,complexity):
        print("init")
        self.name=name 
        self.complexity=complexity
    def show(self):
        print(self.name +" is " +self.complexity)

first=proglang("python","supereasy")
second=proglang("java","easy")

first.show()

second.show()

