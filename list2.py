a=("apple",4,6,"cherry",8,1)
print(a[0])

print(len(a))

print(type(a))

print(a[2:5])
print(a[:5])



a[1:4]=["potato",0]
print(a)

a.insert(9)
print(a)

a.append("carrot")
print(a)

b=(1,2,4)
a.extend(b)

a.pop(4)
print(a)

