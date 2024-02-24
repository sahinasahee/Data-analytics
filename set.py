a={1,2,"apple","mango",7,"apple",88}
print(a)

print(len(a))

print(a)

for i in a:
    print(i)

a.add("cherry")  #list il oru element add akan 
print(a)

b={"banana",33,5.6,2,"guava"} #2list,2set combine cheyyan
a.update(b)
print(b)
print(a)

c=[9,"pink","green",7,8.9]
b.update(c)
print(b)

b.remove("banana") #element remove akan    
print(b)
b.discard(33)
print(b)

#b.remove("banana")
#print(b)

b.discard(33)
print(b)

b.pop() #ramdonly remove   
print(b)

b.clear() #set full pokum  
print(b)

#del b
#print(b)

d={"pink","black",2,5,32,56,"blue",8}
e={2,5,7,9,5,8}  
f=d.union(e)                   
print(f)

d.update(e) 
print(d)

g=d.intersection(e) 
print(g)


h={1,2,3,4,5} #intersection olle verum
i={4,5,6,7,8}
h.intersection_update(i)
print(h)

j=h.difference(i)   
print(j)

set4={1,2,3,4,5,6,7}
set5={1,2}
set6=set4.issubset(set5)
print(set6)
 
set7=set4.issuperset(set5)
print(set7)



