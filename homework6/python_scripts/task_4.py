# Импортируем функцию randint из библиотеки random
from random import randint

# Загадываем случайное число от 1 до 5
random_integer = randint(1, 5)

user_guess = int(input('Я загадал число от 1 до 5. Попробуйте угадать!\nВведите число: '))

# Проверяем введённое число
if user_guess < random_integer:
    print('Слишком мало!')
elif user_guess > random_integer:
    print('Слишком много!')
else:
    print(f'Ты угадал! Загаданное число: {random_integer}')
