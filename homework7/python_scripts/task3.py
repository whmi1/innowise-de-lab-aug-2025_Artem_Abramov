def safe_user_input(prompt: str) -> int:
    """
    Безопасный ввод.
    Гарантирует, что конечным значением будет целое число.
    """
    while True:
        try:
            return int(input(prompt))
        except:
            print('Ошибка: введите целое число')


secret_number = 7
# Переменная для хранения данных, введённых пользователем
user_input = 0

while user_input != secret_number:
    # Получаем число от пользователя
    user_input = safe_user_input('Угадайте число от 1 до 10: ')
    
    # Проверяем его на совпадение
    if user_input == secret_number:
        print('Поздравляю! Вы угадали число!')
    else:
        print('Неверно, попробуйте ещё раз.')
