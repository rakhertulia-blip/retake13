price = int(input("Введите цену одной тетради: "))
quantity = int(input("Введите количество тетрадей: "))

if price > 0 and quantity > 0:
    total = price * quantity
    print("Общая стоимость:", total)
else:
    print("Ошибка: значения должны быть больше 0")
