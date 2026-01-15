'''
260105.양.submission의 Docstring
BFS를 돌면서, 양과 늑대를 count.
BFS가 종료되었을 때, 양과 늑대 숫자를 비교해 살아날 쪽을 더한다.
'''
from collections import deque

R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def inRange(x, y):
    return 0 <= x < R and 0 <= y < C

def canGo(x, y):
    return inRange(x, y) and not visited[x][y] and grid[x][y] != '#'

sheep_left = 0
wolf_left = 0
def bfs(x, y):
    global visited, wolf_left, sheep_left
    wolf = 0
    sheep = 0
    
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    if grid[x][y] == 'v':
        wolf += 1
    elif grid[x][y] == 'o':
        sheep += 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if canGo(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                if grid[nx][ny] == 'v':
                    wolf += 1
                elif grid[nx][ny] == 'o':
                    sheep += 1
    if wolf == 0:
        sheep_left += sheep
    elif sheep == 0:
        wolf_left += wolf
    else:
        if wolf >= sheep:
            wolf_left += wolf
        else:
            sheep_left += sheep

for i in range(R):
    for j in range(C):
        if not visited[i][j] and grid[i][j] != '#':
            bfs(i,j)
print(sheep_left, wolf_left)