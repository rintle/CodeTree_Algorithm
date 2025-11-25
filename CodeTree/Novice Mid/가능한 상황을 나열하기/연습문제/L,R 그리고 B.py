from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
grid = [list(input()) for _ in range(10)]
visited = [[-1 for _ in range(10)] for _ in range(10)]

start = ()
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'L':
            start = (i, j)

def inRange(x, y):
    return 0<=x<10 and 0<=y<10

def canGo(x,y):
    return inRange(x,y) and visited[x][y] < 0 and grid[x][y] != 'R'

q = deque()
q.append(start)
visited[start[0]][start[1]] = 0

while q:
    x, y = q.popleft()
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if canGo(nx,ny):
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
            if grid[nx][ny] == 'B':
                print(visited[nx][ny]-1)
                while q:
                    q.pop()
                break
            
            