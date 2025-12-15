from collections import deque
# BFS 문제
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
isOpen = True

def canOpen(x,y, nx, ny):
    return L <= abs(grid[x][y] - grid[nx][ny]) <= R

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def BFS(x, y):
    global isOpen, visited, grid
    route = []
    pop_sum = 0
    cnt = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        pop_sum += grid[x][y]
        cnt += 1
        route.append((x,y))
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if inRange(nx, ny) and not visited[nx][ny] and canOpen(x,y, nx, ny):
                isOpen = True
                q.append((nx, ny))
                visited[nx][ny] = True

    # update population
    pop_rlt = pop_sum//cnt
    for (x,y) in route:
        grid[x][y] = pop_rlt

ans = 0

while True:
    isOpen=False
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i, j)
    if isOpen:
        ans += 1
    else:
        break
print(ans)
'''
왜 한번에 통과하지 못했지?
52번째줄의 BFS 입력 조건의 Visited 체크를 하지 않아서다.
BFS에서는 항상 visited에 유의하자.
'''