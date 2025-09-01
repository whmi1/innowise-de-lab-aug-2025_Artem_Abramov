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
