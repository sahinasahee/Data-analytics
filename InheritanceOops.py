class person: #parent cls
    def __init__(self,name,age) -> None: 
        self.name=name
        self.age=age
    def myfunction(self):
        print("name",self.name) 
        print("age",self.age)
class child(person):
    pass
x=child("anila",25)
x.myfunction()


#types of inheritance
# 1.single inheritance // single parent single child
# 2.multiple inheritance// 2 or more parent  single child
# 3.multilevel inheritance // one parent then derived class pne um derived class
# 4.hierarchical inheritance// one parent more than one child class
# 5.hybrid inheritance //  pala cases inherit ayi veruna case


class animal:
    def __init__(self,name,sound) -> None:
        self.name=name
        self.sound=sound
    def myfunction(self):
        print("name",self.name)
        print("sound",self.sound)
class cat(animal):
    pass
y=cat("cat","meow")
y.myfunction()


class employee:
    def __init__(self,name,salary) -> None:
        self.name=name
        self.salary=salary
    def myfunction(self):
        print("name",self.name)
        print("salary",self.salary)   
class worker(employee):
    pass
z=worker("raju",560000)
z.myfunction()