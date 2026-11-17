results = [4, 0, 6, 4, 2]

# Добавляем число 10
results.append(10)

# Меняем первый элемент на 5
results[0] = 5

# Удаляем последний элемент
results.pop(2)

# Создаём копию списка
copy_results = results.copy()

# Сортируем копию
sorted_results = sorted(copy_results)

# Преобразуем список в кортеж
my_tuple = tuple(results)

# Выводим результаты
print("Исходный список:", results)
print("Отсортированная копия:", sorted_results)
print("Кортеж:", my_tuple)
print("Первый элемент:", my_tuple[0])
print("Последний элемент:", my_tuple[-1])






