# Запрашиваем у пользователя температуру в градусах Цельсия
degrees_celsius = int(input('Введите температуру в градусах Цельсия: '))

# Вычисляем температуру в градусах Фаренейта по формуле 
degrees_fahrenheit = degrees_celsius * 9 / 5 + 32

print(f'{degrees_celsius}°C это {degrees_fahrenheit}°F')
