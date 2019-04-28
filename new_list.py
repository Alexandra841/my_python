from math import sqrt
a = [2, 4, 9, 16, 25]
y = [sqrt(i) for i in a]
print(y)

list(map((lambda i: sqrt(i)), a))

y = [sqrt(i) for i in [2, 4, 9, 16, 25]]


    
