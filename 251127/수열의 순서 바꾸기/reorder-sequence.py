N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    ans = 0
    for i in range(N-1, 0, -1):
        if nums[i-1] > nums[i]:
            ans += i
            break
    print(ans)