fruits = ["apple", "banana"]

# Добавление "orange" в конец списка
fruits.append("orange")
print(f'Добавление "orange" в конец списка: {fruits}')

# Вставка "grape" по индексу 1
fruits.insert(1, "grape")
print(f'Вставка "grape" по индексу 1: {fruits}')

# Удаление "banana"
del fruits[fruits.index("banana")]
print(f'Удаление "banana": {fruits}')

# Сортировка списка
sorted(fruits)
print(f'Сортировка списка: {fruits}')

# Перевёрнутый список
fruits = fruits[::-1]
print(f'Перевёрнутый список: {fruits}')
