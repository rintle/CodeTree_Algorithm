n, m = map(int, input().split())
nums = list(map(int, input().split()))
possible = [False for _ in range(n)]

ans = 0 
i = 0
while i < n:
    if nums[i]:
        ans += 1
        i += 2*m

    i += 1

print(ans)