s="apple" #string length
b=["cherry"] #tuple
c=("moon")
print(len(s))

print(len(b))

print(len(c))

#overloading is polymorphism de compile type

def add(datatype,*args):
    if datatype=="int":
        ans=0
    elif datatype=="str":
       ans=""
    for i in args:
        ans=ans+i
    print(ans)
add("int",5,6)    
add("str","hello","world")

#overriding is runtime in polymorphism

class a: 
    def fun1(self):
        print("feature 1 of class a")
    def fun2(self):
        print("feature 2 of class a")
class b(a):
    def fun1(self):
        print("modified feature 1 of class a")
    def fun3(self):
        print("feature 3 of class b")    
c=b()
c.fun1()

