a=["apple","rat","cat",3,5]
print(a[0])

#list are ordered,mutable
print(len(a))

print(type(a))

print(a[-1]) #to get last element

print(a[1:])

print(a[1:3])

print(a[0:4])

a[1]="cherry" #for replacing
print(a)

a[2]="guava"
print(a)

a[1:4]="potato","mango" #replace 2 values
print(a)

a.insert(2,"lemon") #
print(a)

# only add an item in last
#1. append  
a.append("carrot")
print(a)

b=[1,2,3,4,5]  #extend
a.extend(b)
print(a)
#pne
print(a)

a.pop(4)
print(a)

a.pop()
print(a)

a.clear()
print(a)

#del b
#print(b)

c=[10,2,6,7,5,9]
for i in c:
    print(i)


#sort method
c.sort()
print(c)  

c.sort(reverse=True)
print(c)

d=c.copy() 
print(d)


e=list(c) #for copy
print(e)

#combine 2 list use +operator
x=c+a 
print(x)

for i in c:
    x.append(i) 
print(x)

c.extend(x) 
print(c)


#comphrehension list 8/02/2023

t=["apple","orange","banana","cherry"]
u=[]
for i in t:
    if "a" in i:
        u.append(i)
print(u)


fruits=["apple","orange","banana","cherry"]
r=[i for i in fruits if "a" in i]
print(r)


n=[i for i in range(0,7)]
print(n)

f=[i for i in range(10)if i<5]
print(f)

n=[i.upper() for i in fruits]
print(n)


