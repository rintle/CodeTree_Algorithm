from collections import deque
N = int(input())
grid = [list(input()) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[False for _ in range(N)] for _ in range(N)]

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

def isGroup(x, y, color):
    return inRange(x, y) and not visited[x][y] and grid[x][y] == color

def findGroup(x, y, color):
    global visited
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if isGroup(nx, ny, color):
                visited[nx][ny] = True
                q.append((nx, ny))
# normal
normal_cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            findGroup(i, j, grid[i][j])
            normal_cnt += 1

# change G to R
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'
            
visited = [[False for _ in range(N)] for _ in range(N)]

# abnormal
abnormal_cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            findGroup(i, j, grid[i][j])
            abnormal_cnt += 1

print(normal_cnt, abnormal_cnt)