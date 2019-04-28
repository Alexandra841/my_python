import random
rand_num = int(random.randint(0,5))
x = 0
while x < 3:
    user = int(input ('Введите число от 0 до 5: '))
    x = x+1
    if user > rand_num:
        print('Попробуйте еще раз!Ваше число больше загаданного')
    elif user < rand_num:
        print('Попробуйте еще раз!Ваше число меньше загаданного')
    elif user == rand_num :
        print('Вы победили!')
        break
if x == 3 and user != rand_num :
    print("Game over! Загаданное число = ", rand_num)
elif x == 3 and user == rand_num :
    print('Вы победили!')
    
