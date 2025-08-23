def safe_float_input(prompt: str) -> float:
    """
    Безопасный ввод чисел. 
    Проверяет, являются ли числом полученные от 
    пользователя данные и возвращает преобразованное число.
    """
    while True:
        try:
            return float(input(prompt))
        except:
            print('Ошибка: введите число, а не текст или символы!')


def safe_operator_input(prompt: str) -> str:
    """
    Безопасный ввод оператора.
    Проверяет оператор на совместимость с существующими.
    Возвращает введённый оператор.
    """
    valid_operators = {'+', '-', '*', '/'}
    while True:
        operator = input(prompt)
        if operator not in valid_operators:
            print('Ошикба: такого оператора не существует!')
        else:
            return operator


# Запрашиваем у пользователя 2 числа
first_int = safe_float_input('Введите первое число: ')
second_int = safe_float_input('Введите второе число: ')
# Запрашиваем оператор для выполнения действия
operator = safe_operator_input('Выберите оператор (+, -, *, /): ')


# Заранее формируем строку для вывода результата
result_line = f'{first_int} {operator} {second_int} = '

# Выполняем необходимые действия в зависимости от выбранного оператора
if operator == '+':
    answer = first_int + second_int
    result_line += str(answer)
    print(f'Результат: {result_line}')
elif operator == '-':
    answer = first_int - second_int
    result_line += str(answer)
    print(f'Результат: {result_line}')
elif operator == '*':
    answer = first_int * second_int
    result_line += str(answer)
    print(f'Результат: {result_line}')
else:
    # Проверка деления на 0
    if second_int == 0:
        print('Делить на 0 нельзя!')
    else:
        answer = round(first_int / second_int, 1)
        result_line += str(answer)
        print(f'Результат: {result_line}')
