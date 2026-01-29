'''
2026.01월.260129.포도주시식.submission의 Docstring
1. 포도주 잔을 선택하면 그 잔에 든 포도주는 모두 마시고, 원래 위치에 두기
2. 연속으로 놓여잇는 3잔을 모두 마실 수는 없음
DP[i]는 i번째 잔 까지 마셨을 때, 마실 수 있는 최대 양의 포도주.

data:  6 10 13  9  8  1
dp:    6 16 19 28  x
dp[i] 가지고는 불가능하다.
i를 하나씩 증가하면서 채워 넣음
i == 0
dp[0][0] : 6
dp[0][1] : 0
i == 1
dp[j][i] : j+1번째로 i번째 잔을 마셨을 때, 마실 수 있는 최대 양의 포도주
dp[0][1] 6 10 
dp[1][1] 0 16 
           ↑ 16 : max( 6+10(두번째로 마시는 경우))
i == 2
               ↓ : 6+13(첫번재로 마시는 경우))
dp[0][i] 6 10 19
dp[1][i] 0 16 23
i==3
                  ↓: 10+9, 16+9
dp[0][i] 6 10 19 25
dp[1][i] 0 16 23 28
i==4
dp[0][i] 6 10 19 25 31
dp[1][i] 0 16 23 28 33

i==5
dp[0][i] 6 10 19 25 31 29
dp[1][i] 0 16 23 28 33 32
맥스는 33
'''
N = int(input())
data = [int(input()) for _ in range(N)]
if N == 1:
    print(data[0])
else:
    dp = [[0 for _ in range(N)]for _ in range(3)]
    dp[0][1] = data[0]
    dp[1][0] = data[0]
    dp[1][1] = data[1]
    dp[2][1] = dp[1][0]+data[1]
    
    for idx in range(2, N):
        # idx 안마셔!
        dp[0][idx] = max(dp[0][idx-1], dp[1][idx-1], dp[2][idx-1])
        # idx가 첫번째!
                        # 이전 잔 안먹음,
        dp[1][idx] = dp[0][idx-1]+data[idx]
        # idx가 두번째!
        dp[2][idx] = dp[1][idx-1]+data[idx]
    print(max(max(dp[0]),max(dp[1]), max(dp[2])))