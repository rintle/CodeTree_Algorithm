n = int(input())
nums = list(map(int, input().split()))

for pos in range(0, 6):
    arr_new = [[] for _ in range(10)]
    for i in range(n):
        div_val = 10**pos
        digit = (nums[i] // div_val)%10
        arr_new[digit].append(nums[i])
    # for i in range(10):
    #     print(f'{i}: {arr_new[i]}')
    store_arr = []
    for i in range(10):
        for num in arr_new[i]:
            store_arr.append(num)
    
    nums = store_arr

for i in store_arr:
    print(i, end=' ')
        