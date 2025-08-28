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

# Получаем размеры прямоугольника
rectangle_height = safe_user_input('Введите высоту прямоугольника: ')
rectangle_width = safe_user_input('Введите ширину прямоугольника: ')

# Отрисовываем прямоугольник, основываясь на полученных данных от пользователя
for i in range(rectangle_height):
    for j in range(rectangle_width):
        print('*', end="")
    print()
