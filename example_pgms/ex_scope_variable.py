#scope variable

x=5
def scope():
    global x
    x=3
    return x

print(x)
print(scope())
print(x)
