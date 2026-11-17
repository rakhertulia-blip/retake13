# Первый список
numbers = [4, 0, 2, 0, 6,8]

total = 0
zero_count = 0
four_count = 0

for i in numbers:
    total = total + i

    if i == 0:
        zero_count = zero_count + 1

    if i >= 4 :
        four_count = four_count + 1

print("Сумма:", total)
print("Количество нулей:", zero_count)
print("Количество чисеЛ БОЛЬШЕ 4:", four_count)

# Второй список
numbers = [0, 0]
numbers.insert(2,5)
print(numbers)
total = 0
count_zero = 0
count_four = 0

for i in numbers:
    total = total + i

    if i == 0:
        count_zero = count_zero + 1

    if i >= 4:
        count_four = count_four + 1

print("Сумма:", total)
print("Количество нулей:", count_zero)
print("Количество чисел от 4:", count_four)

# Пустой список
numbers = []

total = 0
count_zero = 0
count_four = 0

for i in numbers:
    total = total + i

    if i == 0:
        count_zero = count_zero + 1

    if i >= 4:
        count_four = count_four + 1

print("Сумма:", total)
print("Количество нулей:", count_zero)
print("Количество чисел от 4:", count_four)
