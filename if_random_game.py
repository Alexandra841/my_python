import math
import random
rand_num = int(random.randint(0,4))
user = int(input ('Введите число от 0 до 4: '))
if user == rand_num:
    print('Вы победили!')
elif user > rand_num:
    print('Вы проиграли, попробуйте еще раз!Ваше число больше загаданного')
elif user < rand_num:
    print('Вы проиграли, попробуйте еще раз!Ваше число меньше загаданного')
