"""
1 5 6 7

1장만 산다면 - 1원
2장 산다면 - 5원
3장 산다면 - 1+5 || 6 6원
4장 산다면 - 7, 5+5, 6+1 ? 10.

10
1 2 3 4 5 6 7  8  9  10
1 1 2 3 5 8 13 21 34 55
[] [1] [2] [3] [4] [5] [8] [13] [21] [34] [55]
dp[1] = 1
dp[2] = max(price[2], dp[1]+dp[1])
dp[3] = max(price[3], dp[2]+dp[1])
dp[4] = max(price[4], dp[3]+dp[1], dp[2]+dp[2] dp[1]+dp[3])
dp[5] = max(price[5], dp[4]+dp[1], dp[3]+dp[2])
dp[6] = max(price[6], dp[5]+dp[1], dp[4]+dp[2], dp[3]+dp[3])
"""
price = [0 for _ in range(1001)]
N = int(input())
tmp = list(map(int, input().split()))
for i in range(1, N+1):
    price[i] = tmp[i-1]
DP = [0 for _ in range(1000)]
DP[1] = price[1]

for i in range(2, N+1):
    tmp = 0
    for j in range(1, i//2+1):
        tmp = max(tmp, DP[i-j]+DP[j])
    DP[i] = max(price[i], tmp)
print(DP[N])