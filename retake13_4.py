def add_bonus(points, bonus):
    result = points + bonus
    if points >= 10:
        print("Сдано")
    else:
        print("Не сдано")
    return result
# Основная программа
result = add_bonus(8, 1)
#status = get_status(result)

print("Баллы:", result)
#print("Результат:", status)


result = add_bonus(8, 2)
#status = get_status(result)

print("Баллы:", result)
#print("Результат:", status)


result = add_bonus(14, 0)
#status = get_status(result)

print("Баллы:", result)
#print("Результат:", status)
