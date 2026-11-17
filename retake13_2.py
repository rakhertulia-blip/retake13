group = input("Введите группу: ")
age = int(input("Введите возраст: "))

group = group.strip()
group = group.upper()

if age < 14:
    print("Отказ: возраст меньше 14 лет")
elif group !="Т118" :
    print("Отказ: неправильная группа")
else:
    print("Участие разрешено")
