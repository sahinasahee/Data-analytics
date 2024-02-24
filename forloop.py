a=[1,2,3,4,5]
for i in a:
    print(i)
    if i==4:
        break

for i in a: 
    if i==3:
        continue #continue kodukkune ee "3" ozhich bakki ellam print akum
    print(i)
    
x=1
while x<10:  #10 ethunna vere it check cheyythond irikkum while
    print(x)
    x+=1 #increment

x=1
while x<6:
    print(x)
    if x==3:
        break
    x+=1 

x=11
while x<17:
    x+=1
    if x==14:
        continue
    print(x)

