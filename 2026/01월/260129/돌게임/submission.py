'''
2026.01월.260129.돌게임.submission의 Docstring
1 또는 3을 집는 상태.
DP[i]는 i번째일 때, 주을 수 있는 최대 돌 개수.
DP[i] = DP[i-1]+3 or DP[i-1]+1


Real DP
DP[i] = 돌이 i개 있을 때, 우승 여부
DP[i] = 1 : 돌이 i개 있을 때, 시작하면 우승
DP[i] = 0 : 돌이 i개 있을 때, 시작하면 패배
'''
N = int(input())

dp = [0 for _ in range(N+3)]
dp[1] = 1
dp[2] = 0
dp[3] = 1
for i in range(4, N+1):
    if dp[i-1] == 0 or dp[i-3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0
print("SK" if dp[N] else "CY")


# # 내가 풀이한 방식은 시뮬레이션
# N = int(input())
# DP = [0 for i in range(N+1)]
# cnt = 1
# while True:
#     DP[cnt] = DP[cnt-1]+3 if DP[cnt-1]+3 < N else DP[cnt-1]+1
#     if DP[cnt] == N:
#         break
#     cnt += 1
# if cnt % 2 == 1:
#     print("SK")
# else:
#     print("CY")