import random
import math

def find_sum_between_min_max(arr):
    """
    Функция находит сумму отрицательных элементов, расположенных
    между минимальным и максимальным элементами массива
    """
    # Шаг 1: Обработка краевых случаев
    if not arr:  # Проверка на пустой массив
        print("Массив пуст.")
        return 0
    if len(arr) == 1:  # Если только один элемент
        print("В массиве только один элемент.")
        return 0

    # Шаг 2: Поиск индексов минимального и максимального элемента
    min_index = 0
    max_index = 0
    min_value = arr[0]
    max_value = arr[0]

    for i, value in enumerate(arr):
        if value < min_value:
            min_value = value
            min_index = i
        if value > max_value:
            max_value = value
            max_index = i

    print(f"Минимальный элемент: arr[{min_index}] = {min_value}")
    print(f"Максимальный элемент: arr[{max_index}] = {max_value}")

    # Шаг 3: Определение границ интервала
    left_index = min(min_index, max_index)
    right_index = max(min_index, max_index)

    print(f"Интервал между ними (включая границы): [{left_index}:{right_index}]")

    # Шаг 4: Вычисление суммы отрицательных элементов в интервале
    total_sum = 0
    found_negative = False

    # Проход по элементам от left_index до right_index включительно
    for i in range(left_index, right_index + 1):
        if arr[i] < 0:
            total_sum += arr[i]
            found_negative = True
            print(f"  Найден отрицательный элемент: arr[{i}] = {arr[i]} (текущая сумма: {total_sum})")

    # Шаг 5: Вывод результата
    if not found_negative:
        print("В указанном интервале нет отрицательных элементов.")
        return 0
    else:
        print(f"Итоговая сумма отрицательных элементов: {total_sum}")
        return total_sum


# --- Основная часть программы ---
if __name__ == "__main__":
    # Генерация тестового массива для демонстрации
    N = 15  # Размерность массива
    # Генератор массива со случайными числами от -20 до 30
    A = [random.randint(-20, 30) for _ in range(N)]

    print("Исходный массив:")
    print(f"Индексы: {list(range(N))}")
    print(f"Значения: {A}")
    print("-" * 50)

    # Вызов функции для решения задачи
    result = find_sum_between_min_max(A)

    print("\n" + "=" * 50)
    print(f"ОТВЕТ: Сумма отрицательных элементов между мин и макс = {result}")