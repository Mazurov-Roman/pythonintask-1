#Задача 6. Вариант 16
#Создайте игру, в которой компьютер загадывает имя одной из шести официальных жен Ивана IV Грозного, а игрок должен его угадать.

#Mazurov R.V.
#30.03.2016
print('Угадайте имя одной из шести официальных жен Ивана IV Грозного, которую загадал компьютер')
import random
a = random.choice(['Анастасия', 'Мария', 'Марфа', 'Анна', 'Анна', 'Мария'])
b = input('Ваш ответ: ')

b=''
while a !=b : 
	print ('Вы не угадали')
	b = input('Ваш ответ: ')

print ('Вы угадали: ' + a + ' - ' + b)
input('\nНажмите Enter для выхода')