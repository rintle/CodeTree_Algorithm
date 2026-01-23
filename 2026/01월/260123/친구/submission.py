'''
2026.01월.260123.친구.submission의 Docstring
가장 유명한 사람 : 각 사람의 2-친구를 구하면 됨.
A가 B의 2-친구가 되기 위한 조건
1. A와 B가 친구
2. A, B와 모두 친구인 C가 있어야 함
'''
N = int(input())
grid = [[0 for _ in range(N)]for _ in range(N)]

for x in range(N):
    data = input()
    for y in range(N):
        if data[y] =='Y':
            grid[x][y] = 1
ans = 0
for x in range(N):
    cnt = 0
    for y in range(N):
        if grid[x][y]:
            cnt += 1
            continue
        if x != y:
            for k in range(N):
                if grid[x][k] and grid[k][y]:
                    cnt +=1
                    break
    ans = max(ans, cnt)
print(ans)