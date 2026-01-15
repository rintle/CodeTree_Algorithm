n = int(input())
n+=1
arr = [0]+list(map(int, input().split()))
def heapify(arr, n, idx):
    largest = idx
    left=idx * 2
    right = idx*2+1

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify(arr, n, largest)
for i in range(n//2, 0, -1):
    heapify(arr, n, i)

for i in range(n-1, 0, -1):
    arr[i], arr[1] = arr[1], arr[i]
    n -= 1
    heapify(arr, n, 1)

print(*arr[1:])