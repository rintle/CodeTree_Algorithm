'''
Docstring for 2026.02월.260217.치즈
0,0에서 BFS하면서, cheese에 cnt 1씩 증가시킴.
2 이상인 것들에 대해서만 녹이면 됨
let's go
'''
from collections import deque
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

hasCheese = True
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def inRange(x, y):
    return 0<= x < N and 0<= y < M

def BFS():
    global grid, hasCheese
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0,0))
    hasCheese = False
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if inRange(nx, ny):
                if grid[nx][ny] == 0:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                else:
                    visited[nx][ny] += 1
                    hasCheese = True
    
    for x in range(N):
        for y in range(M):
            if visited[x][y] >= 2:
                grid[x][y] = 0
answer = 0
while True:
    BFS()
    if not hasCheese:
        break
    answer += 1
print(answer)
    