from collections import deque
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# print('='*30)
# for g in grid:
#     print(*g)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

cheeseLeft = 0
for i in range(N):
    cheeseLeft += sum(grid[i])

def inRange(x, y):
    return 0 <= x < N and 0 <= y < M

def findOutLine():
    global grid
    visited = [[False for _ in range(M)] for _ in range(N)]
    outLine = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if inRange(nx, ny) and not visited[nx][ny]:
                # print(nx, ny)
                if grid[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                else:
                    outLine[nx][ny] = True
    
    cheeseLeft = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                if outLine[i][j]:
                    grid[i][j] = 0
                else:
                    cheeseLeft += 1
    return cheeseLeft

def melt():
    return findOutLine()

cnt = 0
prevCheese = cheeseLeft
while True:
    cheeseLeft = melt()
    if cheeseLeft==0:
        print(cnt+1)
        print(prevCheese)
        break
    prevCheese = cheeseLeft
    cnt += 1