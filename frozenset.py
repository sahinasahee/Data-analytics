x=("red","blue","grey")
y=frozenset(x) # frozenset is immutable
print(y)

x[0]=3
print(y)