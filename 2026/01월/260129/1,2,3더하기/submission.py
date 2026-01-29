'''
2026.01월.260129.1,2,3더하기.submission의 Docstring
정수 4를 1,2,3의 합으로 나타내는 방법은 총 7가지가 있다.
정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법
DP[i] = 나타내는 경우의 수
DP[1] = 1
DP[2] = 2
DP[3] = 4
DP[4] = 7
DP[i] = DP[i-1] (+1) + DP[i-2] (+2) + DP[i-3] (+3)
'''
T = int(input())
DP = [0 for _ in range(12)]
DP[1]=1;DP[2]=2;DP[3]=4
for i in range(4, 12):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
ans = []
for _ in range(T):
    n = int(input())
    ans.append(str(DP[n]))
        
print('\n'.join(ans))