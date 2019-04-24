s = "У лукоморья 123 дуб зеленый 456"
#1
s.count('я')
print(s.index('я'))

#2
s.count('у')

#3
if s.isalpha()== False:
    print(s.upper())

#4
len(s)
if len(s) > 4:
    print(s.lower())

#5
m = list(s)
m[0] = 'О'
s = ''. join(m)
m
print(s)
