import random
s =  ['самовар', 'весна', 'лето']
word = random.choice(s)
word1 = word
ps = list(word)
letter = random.choice(ps)
index = ps.index(letter)
ps[index] = '?'
word = ''.join(ps)
print(word)
user = str(input('Введите букву: '))
if user == letter:
    print('Вы угадали!')
else:
    print('Увы, Вы проиграли!Загаданное слово: ', word1)
