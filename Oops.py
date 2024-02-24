class python:
    a=5
b=python()
print(b.a)

class person:
    def __init__(self,name,age) -> None:
        pass 
        self.name=name
        self.age=age
p=person("nena",24)
print(p.name) 
print(p.age)  


class person:
    def __init__(self,name,age) -> None: 
        self.name=name
        self.age=age
    def myfunction(self): #myfunction=object
        print("my name is",self.name)
        print("age",self.age)
a=person("sana",28)    #person = class /   name,age =property
a.myfunction()  


