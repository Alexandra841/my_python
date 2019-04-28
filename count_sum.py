x = input("Введите число: ")
c = 0
for i in x:
    if int(i) % 2 != 0:
        c +=pow(int(i),2)
print("Cумма квадратов нечетных цифр в числе = ",c)

