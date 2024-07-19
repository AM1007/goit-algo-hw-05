def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def exist_in_list(arr, x):
    return linear_search(arr, x) != -1

if __name__ == "__main__":
    arr = [5, 3, 8, 1, 4]
    print(arr, linear_search(arr, 9))
    print(exist_in_list(arr, 5))
            
