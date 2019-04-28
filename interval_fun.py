x = []
for i in range(10,30,2):
    x.append(i)
y = [i**2 + 3 for i in x]
c = sum(y)
print(c)
