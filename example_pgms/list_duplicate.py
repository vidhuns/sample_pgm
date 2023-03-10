a = [1, 1, 1, 2, 3, 4, 5]
b = []
for item in a:
    if item not in b:
        b.append(item)

print(b)