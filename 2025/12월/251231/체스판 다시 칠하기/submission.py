'''
251231.체스판 다시 칠하기.submission의 Docstring
8x8만큼 순회하면서 B, W개수를 세고
B가 좌상일 떄, W가 좌상일 때 개수에서 변해야 하는 개수를 알아낸 뒤
최솟값을 return하게 하면 된다.
아니다. 개수체크만 하는거로는 의미가 없다.
진짜 배열이 맞는지 확인해야한다.
'''
N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

def checkBoard(x, y):
    r_val = 2500
    # 좌상단이 W인 경우
    cnt = 0
    for i in range(x, x+8, 2):
        for j in range(y, y+8, 2):
            if grid[i][j] == 'B':
                cnt += 1
        for j in range(y+1, y+8, 2):
            if grid[i][j] == 'W':
                cnt += 1
    for i in range(x+1, x+8, 2):
        for j in range(y, y+8, 2):
            if grid[i][j] == 'W':
                cnt += 1
        for j in range(y+1, y+8, 2):
            if grid[i][j] == 'B':
                cnt += 1
    r_val = min(r_val, cnt)
    # 좌상단이 B인 경우
    cnt = 0
    for i in range(x, x+8, 2):
        for j in range(y, y+8, 2):
            if grid[i][j] == 'W':
                cnt += 1
        for j in range(y+1, y+8, 2):
            if grid[i][j] == 'B':
                cnt += 1
    for i in range(x+1, x+8, 2):
        for j in range(y, y+8, 2):
            if grid[i][j] == 'B':
                cnt += 1
        for j in range(y+1, y+8, 2):
            if grid[i][j] == 'W':
                cnt += 1
    return min(r_val, cnt)
ans = 2500
# 시작점 찾기
for i in range(N-7):
    for j in range(M-7):
        ans = min(ans, checkBoard(i,j))
print(ans)