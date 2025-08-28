scores = [75, 88, -10, 95, 100, -25, 89]
total_score = 0

print("Для scores = [75, 88, -10, 95, 100, -25, 89]")

for score in scores:
    # Проверка, если балл < 0
    if score < 0:
        continue
    # Проверка, если балл == 0
    elif score == 0:
        break
    # В остальных случаях добавляйте балл к total_score
    else:
        total_score += score

    print(f"Добавлен балл: {score}")
# если цикл не был прерван, выводим сообщение "Все данные обработаны"
else:
    print("Все данные обработаны")

print(f"\nИтоговая сумма баллов: {total_score}")
