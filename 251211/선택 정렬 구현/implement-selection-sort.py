n = int(input())
nums = list(map(int, input().split()))

for i in range(n-1):
    smallest = i
    for k in range(i+1, n):
        if nums[smallest] > nums[k]:
            smallest = k
    if i != smallest:
        nums[i], nums[smallest] = nums[smallest], nums[i]
for num in nums:
    print(num, end=' ')