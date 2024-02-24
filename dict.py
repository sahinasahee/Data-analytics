student={"name":[2,"mango"],"age":20,"place":"goa"}
print(student)
print(student["name"])

print(len(student))

x=student.get("name")
print(x)

y=student.keys()
print(y)

z=student.values()
print(z)

a=student.items()
print(a)

student["age"]=76 #value change akkan
print(student)

student.update({"age":30}) #value change akkan
print(student)

student.update({"course":"DA"})
print(student)

student["mark"]=11
print(student)

student.pop("name")
print(student)

student.popitem() #last itm revome
print(student)


del student["age"]
print(student)

student.clear()
print(student)

student1={"name":[2,"mango"],"age":20,"place":"goa"}
student2=student1.copy()
print(student2)


#nested dictonary

class1={"child1":{"name":"achu","age":7},
        "child2":{"name":"pachu","age":9}
        }
print(class1)

print(class1["child1"]["age"])


#task set create union

for i in student1:
    print(i)
    print(student1[i])

for x in student1.keys():
    print(x)

for x in student1.values():
    print(x)

for x,y in student1.items():
    print(x,y)



                        