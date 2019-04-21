value = input("Введите номер: ")
if value:
    номер = int(value)
    if номер == 3:
        print("Li")
    elif номер == 17:
        print("Cl")
    elif номер == 25:
        print("Mn")
    elif номер == 80:
        print("Hg")
    else:
        print("Неизвестный элемент")
else:
    print("Введите значение номера элемента")
