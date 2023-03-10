import copy
x = [1, 2, 3]
y = copy.deepcopy(x)
print (y)
z= copy.copy(x)
print(z)
x.insert(4,"Test")
print(y)
print(x)
print(z)