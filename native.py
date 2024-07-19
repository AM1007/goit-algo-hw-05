def native_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    #Перебір символів головного рядка
    for i in range(N - M + 1):
        j = 0

        # Перебір по символах підрядка
        while j < M:
            if main_string[i + j] != pattern[j]:
                break
            j += 1

        # Якщо значення дорівнює довжині підрядка, то підрядок знайдено
        if j == M:
            return i
    return -1

main_string = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
position = native_search(main_string, pattern)

if position != -1:
    print(f"Підрядок знайдено на позиції {position}")
else:
    print("Пыдрядок знайдено в головному рядку")
