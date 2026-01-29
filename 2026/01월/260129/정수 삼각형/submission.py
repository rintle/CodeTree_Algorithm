'''
2026.01월.260129.정수 삼각형.submission의 Docstring
트리를 이용하는 문제로 보여짐
예
  7 3 8 8 1 0 2 7 4 4 4 5 2 6 5
이렇게 들어있는거고,
DP[i] = 거기까지의 최대 합인 경우.
0 7 10 15 18 16 15 . . .
이렇게 가는거지.
tree의 특징은
idx * 2를 하면 왼쪽
idx * 2 + 1을 하면 오른쪽임.
예
  7 3 8 8 1 0 2 7 4 4 4 5 2 6 5
0 1 2 3 4 5 6 7 8 9 ...
반대로, child node에서 생각했을 때
idx //2를 하면 왼쪽 parent
idx //2+1을 하면 오른쪽 parent.
단, 결과가 idx보다 클 수 없다.
예) idx 4의 경우 (왼쪽 부모 없음)
idx//2 == 2
아래 두 경우는 불가능함.
idx//2 - 1 = 1
idx//2 + 1 = 3 

예) idx 5의 경우
idx//2 == 2
idx//2 + 1 = 3 

예) idx 6의 경우 (오른쪽 부모 없음)
idx//2 == 3
아래 두 경우는 불가능함.
idx//2 - 1 = 1
idx//2 + 1 = 3 

거꾸로 올라가지 말고, 앞에서 부터 채워나간다는 느낌으로
DP[i*2] = max(DP[i*2], DP[i*2]+DP[i])
DP[i*2+1] = max(DP[i*2+1], DP[i*2+1]+DP[i])
X 이건 Binary Tree가 아님.

같은 rank인것도 신경 써야 하는데 . . .
'''
N = int(input())
dp = [[0 for _ in range(N+1)] for _ in range(N)]
data = [list(map(int, input().split())) for _ in range(N)]
dp[0][0] = data[0][0]
for rank in range(1, N):
    for n in range(len(data[rank])):
        # 왼쪽 부모 체크
        if n-1 >= 0:
            dp[rank][n] = max(dp[rank][n], data[rank][n]+dp[rank-1][n-1])
        # 오른쪽 부모 체크
        
        dp[rank][n] = max(dp[rank][n], data[rank][n]+dp[rank-1][n])
print(max(dp[-1]))