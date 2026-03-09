import random

# Генерируем массив
N = 15
A = [random.randint(-20, 30) for _ in range(N)]
print("Массив:", A)

# Проверка на количество элементов
if len(A) < 2:
    print("В массиве меньше двух элементов. Невозможно найти интервал между минимумом и максимумом.")
    sum_negative = 0
else:
    # Находим индексы минимума и максимума
    i_min = A.index(min(A))
    i_max = A.index(max(A))
    
    # Определяем границы интервала
    left = min(i_min, i_max)
    right = max(i_min, i_max)
    
    # Суммируем отрицательные элементы в интервале
    sum_negative = sum(x for i, x in enumerate(A) if left <= i <= right and x < 0)
    
    print(f"Индексы: мин={i_min} ({A[i_min]}), макс={i_max} ({A[i_max]})")
    print(f"Интервал: [{left}:{right}]")

print(f"Сумма отрицательных: {sum_negative}")

