n = int(input())
arr = list(map(int, input().split()))

def partition(arr, low, high):
    # print(arr)
    # print(low, high)
    pivot = arr[high]
    # print(pivot)
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quicksort(arr, low, high):
    if low < high:
        pos = partition(arr, low, high)
        quicksort(arr, low, pos-1)
        quicksort(arr, pos+1, high)

quicksort(arr, 0, n-1)
print(*arr)