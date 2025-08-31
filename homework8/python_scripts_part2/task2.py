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
