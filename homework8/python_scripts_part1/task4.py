words = ["hello", "world", "python", "code"]

# Создание списка длин слов с помощью генератора списков
words_length = [len(word) for word in words]
print(f'Список длин слов: {words_length}')

# Создание списка слов, содержащих более 4 символов
words_length_more_than_four = [word for word in words if len(word) > 4]
print(f'Список слов, длина которых больше 4: {words_length_more_than_four}')

# Создание словаря с парами {слово : длина слова}
words_dict = {}

for i in range(len(words)):
    words_dict[words[i]] = words_length[i]

print(f'Словарь слов с их длинами: {words_dict}')
