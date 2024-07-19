def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        
        mid = (high + low) // 2

        # якщо значення х більше за значення посередині списку, ігноруємо ліву пооловину 
        if arr[mid] < x:
            low = mid + 1
        
        # якщо значення х меньше за значення посередині списку, ігноруємо праву пооловину
        elif arr[mid] > x:
            high = mid - 1
        
        # інакше x присутній на позиції і повертаємо його
        else:
            return mid
        
    # якщо елемент не знайдений
    return -1

arr = [2, 3, 4, 10, 40]
x = 3

result = binary_search(arr, x)
if result != -1:
    print(f"Elemet present at index {result}")
else:
    print(f"Elemet is not present in array")


import matplotlib.pyplot as plt
import numpy as np

# Визначаємо кількість елементів та відповідні кроки для лінійного та двійкового пошуку
n = np.arange(1, 21)
linear_search_steps = n
binary_search_steps = np.log2(n)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(n, linear_search_steps, label='Linear Search', color='blue')
plt.plot(n, binary_search_steps, label='Binary Search', color='green')
plt.xlabel('Number of elements (n)')
plt.ylabel('Number of steps')
plt.title('Comparison of Linear and Binary Search')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Відображення графіка
plt.show()
