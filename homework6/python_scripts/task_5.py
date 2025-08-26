# Запрашиваем у пользователя число
user_input = int(input('Введите число: '))

# Проверяем его на чётность/нечётность
if user_input % 2 == 0:
    print(f'Число {user_input} - чётное.')
else:
    print(f'Число {user_input} - нечётное.')
