a="hello "
print(a)

#slicing
print(a[2])
print(a[0])

print(len(a))

print(a[:2])  #from beginning but not includimg element at index 2
print(a[1:4])
print(a.upper())

b="MICROMAX"
print(b.lower())

c="  money"
print(c.strip()) #to remove spaceof start & end

d= "sahena ps"
print(d.strip()) #middle olle space kalayila

e="hello,world"
print(e.split(","))

f="hellow,orld"
print(f.split(","))

print(f.replace("h","j"))

#concantination
i="cyberspace"
j="cryptography"
k=i+" "+j  #combine 
print(k)


#count method

g="hello world hello"
h=g.count("hello")
print(h)


h="hello world hello"
i=h.capitalize() #fir
print(i)

j=h.index("world")
print(j)