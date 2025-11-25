N = int(input())
nums = list(map(int, input().split()))

cnt = 0
second = 100
idx = -1
min_num = min(nums)
for i in range(N):
    if nums[i] > min_num:
        if nums[i] < second:
            second = nums[i]
            idx = i
            cnt = 0
        elif nums[i] == second:
            cnt += 1

if cnt:
    print(-1)
else:
    if idx < 0:
        print(idx)
    else:
        print(idx+1)