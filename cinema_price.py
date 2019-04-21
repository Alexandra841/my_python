film = input('Выберете фильм : ')
if film:
    if film == "Пятница" :
        day = input('Выберете день : ')
        if day == "Сегодня" :
            time = input('Укажите время : ')
            if time == "12":
                price = 250
            elif time == "16":
                price = 350
            elif time == "20":
                price = 450
        elif day == "Завтра":
            disc = 0.05
            time = input('Укажите время : ')
            if time == "12":
                price = 250 * (1 - disc)
            elif time == "16":
                price = 350* (1 - disc)
            elif time == "20":
                price = 450* (1 - disc)

    elif film == "Чемпионы" :
        day = input('Выберете день : ')
        if day == "Сегодня" :
            time = input('Укажите время : ')
            if time == "10":
                price = 250
            elif time == "13":
                price = 350
            elif time == "16":
                price = 350
        elif day == "Завтра":
            disc = 0.05
            time = input('Укажите время : ')
            if time == "10":
                price = 250 * (1 - disc)
            elif time == "13":
                price = 350* (1 - disc)
            elif time == "16":
                price = 350* (1 - disc)
                
    elif film == "Пернатая банда" :
        day = input('Выберете день : ')
        if day == "Сегодня" :
            time = input('Укажите время : ')
            if time == "10":
                price = 350
            elif time == "14":
                price = 450
            elif time == "18":
                price = 450
        elif day == "Завтра":
            disc = 0.05
            time = input('Укажите время : ')
            if time == "10":
                price = 350 * (1 - disc)
            elif time == "14":
                price = 450* (1 - disc)
            elif time == "18":
                price = 450* (1 - disc)
    else:
        print ("Сеанс не найден, проверьте правильнось ввода")
else:
    print ("Сеанс не найден, проверьте правильнось ввода")
        
number = int(input('Укажите количество билетов : '))
if number:
    if number >= 20:
        discount = 0.20
        print ("Общая стоимость билетов равна: " , price * number * (1 - discount) , "руб." )
        print ("Ваши билеты забронированы! Спасибо за использование нашего сайта, ждем Вас снова! " )
    else:
        print ("Общая стоимость билетов равна: " , price * number , "руб." )
        print ("Ваши билеты забронированы! Спасибо за использование нашего сайта, ждем Вас снова! ")
else:
    print ("Error")
