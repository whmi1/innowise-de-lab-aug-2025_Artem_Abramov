# Импортируем модуль из библиотеки для вывода с задержкой
from time import sleep


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


user_input = safe_user_input('Введите число для обратного отсчёта: ')

for i in range(user_input, 0, -1):
    # Выводим каждое число с задержкой в 1 секунду между каждым
    print(f"{i}...")
    sleep(1.0)

print('Go!')
