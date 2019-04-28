a = 0
while True:
    x = input("Введите число или стоп для выхода: ")
    if x.lower() == "стоп":
        print("Выход из программы! До встречи!")
        break
    else:
        if x.isdigit():
            a +=int(x)
        else:
            print("Что это?")

print("Сумма равна = ", a)
