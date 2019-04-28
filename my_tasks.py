print("Простой todo: 1. Добавить задачу. 2. Вывести список задач. 3. Выход") 
time= []
category = []
task = []
while True:
    num = input("Введите число или выход: " )
    if num == "1" :
        task.append(input("Сформулируйте задачу: "))
        category.append(input("Добавьте категорию к задаче: "))
        time.append(input("Добавьте время к задаче: "))
    elif num == "2":
        for i in range(len(task)):
            print ("Задача: ", task[i], "Категория: ", category[i], "Время: ",time[i])
    elif num == "выход":
        print("Выход из программы! До встречи!")
        break
        
        
        
    
    
    
    
    
