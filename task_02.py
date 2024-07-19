def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Повернення верхнєї межі по закінчуенні циклу, якщо цілі не знайдено  
    return (iterations, upper_bound)

# Приклад використання
arr = [1.1, 2.3, 3.5, 4.7, 6.8, 7.9, 8.2]
target = 5.0

result = binary_search(arr, target)
print(f"Кількість ітерацій: {result[0]}")
print(f"Верхній поріг: {result[1]}")
