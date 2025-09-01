# Часть 1: Строки, Списки, Словари
## Упражнение 1: Операции со строкой
### Описание упражнения:
Дана строка: "Python Programming". Напишите код, который:
1. Выводит длину строки
2. Выводит символ по индексу 7
3. Выводит последние 3 символа
4. Проверяет, содержится ли в строке подстрока "gram"
### Код:
```
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

```
### Результат:
![Часть 1. Упражнение 1](part1_task1.png)

## Упражнение 2: Методы строк и форматинг
### Описание упражнения:
Дано: email = " USER@DOMAIN.COM "
1. Очистить и отформатировать до вида: "user@domain.com"
2. Разделить на имя пользователя и домен
3. Используя f-строку, создать: "Username: user, Domain: domain.com"
### Код:
```
email = " USER@DOMAIN.COM "
  
# Очищаем и форматируем строку
clean_email = email.strip().lower()
  
# Отделяем имя пользователя и домен
user_name = clean_email[:clean_email.find("@")]
domain = clean_email[clean_email.find("@") + 1:]
  
print(f"Username: {user_name}, Domain: {domain}")

```
### Результат:
![Часть 1. Упражнение 2](part1_task2.png)

## Упражнение 3:  Методы списка
### Описание упражнения:
Исходный список: fruits = ["apple", "banana"]
Выполните следующие операции по порядку:
1. Добавьте "orange" в конец списка
2. Вставьте "grape" по индексу 1
3. Удалите "banana"
4. Отсортируйте список
5. Переверните список
После каждого шага выводите список на печать
### Код:
```
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

```
### Результат:
![Часть 1. Упражнение 3](part1_task3.png)

## Упражнение 4: List comprehensions и словари
### Описание упражнения:
Дано: words = ["hello", "world", "python", "code"]
1. Создать список длин слов, используя списковое включение 
2. Создать список слов длиннее 4 символов
3. Создать словарь: {слово : длина} для всех слов
### Код:
```
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

```
### Результат:
![Часть 1. Упражнение 4](part1_task4.png)

## Упражнение 5 (Опционально): Two Sum
### Описание упражнения:
Дан список чисел **nums** и целевое число **target**. Найти индексы двух чисел, сумма которых равна **target**.
### Код:
```
nums = [2, 7, 11, 15]
target = 9
nums_map = {}
result = []
  
for i in range(len(nums)):
    difference = target - nums[i]
    if difference in nums_map:
        result = [nums_map[difference], i]
        break
    nums_map[nums[i]] = i    
  
print(f'nums = {nums}\ntarget = {target}')
  
if not result:
    print("Таких чисел нет в списке.")
else:
    print(f'Ответ: {result}')
    
```
### Результат:
![]() ![Часть 1. Упражнение 5](part1_task5.png)

# Часть 2: Функции и ООП
## Упражнение 1: Функции без параметров
### Описание упражнения:
Создайте функцию без параметров show_current_time() — печатает текущие дату и время (используйте модуль datetime).
### Код:
```
# Импортируем библиотеку для доступа к текущей дате и времени
import datetime
  
# Функция для показа текущей даты и времени
def show_current_date():
    print(datetime.datetime.now())
  
show_current_date()

```
### Результат:
![Часть 2. Упражнение 1](part2_task1.png)

## Упражнение 2: Функции с параметрами
### Описание упражнения:
Дан повторяющийся код расчёта цены с НДС:
```
prices = [1000, 3499, 250]
nds = 0.20
print(prices[0] + prices[0] * nds)
print(prices[1] + prices[1] * nds)
print(prices[2] + prices[2] * nds)
```
Задание:
1. Вывести расчёт в функцию add_vat()
2. Примените её ко всем элементам списка в цикле и распечатайте итоговые цены, используйте цикл.
### Код:
```
# Функция вычисления цены с учётом НДС
def add_vat(price: int) -> float:
    nds = 0.2
    return price + price * nds

  
prices = [1000, 3499, 250]
  
print('Цены без учёта НДС:', prices)
  
# Применнеие функции ко всем ценам
for i in range(len(prices)):
    prices[i] = add_vat(prices[i])
  
print('Ценыс учётом НДС:', prices)

```
### Результат:
![Часть 2. Упражнение 2](part2_task2.png)

## Упражнение 3 (Опционально): Вычисление средней оценки
### Описание упражнения:
- Создайте функцию calculate_average_score(), которая будет вычислять средний балл.
- Функция должна принимать список оценок scores как обязательный аргумент.
- Добавьте опциональный булевый параметр ignore_lowest со значением по умолчанию False.
- Если ignore_lowest равен True, функция должна отбросить наименьшую оценку перед вычислением среднего. Если в списке всего одна оценка, отбрасывать её не нужно.
- Используя цикл, пройдитесь по списку student_data. 2 раза, первый раз учитывая все оценки, а второй раз отбросив худшие оценки
### Код:
```
# Функция вычисления среднего балла
def calculate_average_score(scores: list, ignore_lowes=False) -> float:
    if ignore_lowes and len(scores) > 1:
        del scores[scores.index(min(scores))]
        return round(sum(scores) / len(scores), 2)
    return round(sum(scores) / len(scores), 1)

  
students_data = [
    {'name': 'Алексей', 'scores': [85, 92, 78, 95]},
    {'name': 'Марина', 'scores': [65, 70, 58, 82]},
    {'name': 'Светлана', 'scores': [98, 95, 100]},
    {'name': 'Алёша', 'scores': [89]}
]
  
# Первый проход по циклу: параметр ignore_lowes = False
print('Подсчёт среднего среднего балла на основе всех оценок:')
  
for data in students_data:
    print(f'{data['name']}: {calculate_average_score(data['scores'])}')
  
# Первый проход по циклу: параметр ignore_lowes = True
print('Подсчёт среднего балла, игнорируя минимальную оценку:')
  
for data in students_data:
    print(f'{data['name']}: {calculate_average_score(data['scores'], True)}')
    
```
### Результат:
![Часть 2. Упражнение 2](part2_task3.png)