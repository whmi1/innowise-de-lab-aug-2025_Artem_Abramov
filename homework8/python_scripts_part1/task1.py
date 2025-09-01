line = "Python Programming"
print(f"Изначальная строка: {line}")

# Вывод длины строки
print(f"Длина строки: {len(line)}")

# Вывод символа по индексу 7
print(f"Символ по индексу 7: {line[7]}")

# Вывод последних 3 символов
print(f"Последние 3 символа: {line[-3:]}")

# Проверка на содержание в строке подстроки "gram"
print(f'Содержание подстроки "gram": {True if line.find("gram") != -1 else False}')
