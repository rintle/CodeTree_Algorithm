n = int(input())
nums = list(map(int, input().split()))

for pos in range(5, -1, -1):
    arr_new = [[] for _ in range(10)]
    for i in range(n):
        div_val = 10**pos
        digit = nums[i] // div_val
        arr_new[digit].append(nums[i])
    store_arr = []
    for i in range(10):
        for num in arr_new[i]:
            store_arr.append(num)
    nums = store_arr
    
for i in store_arr:
    print(i, end=' ')
        