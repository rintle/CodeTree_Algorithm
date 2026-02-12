'''
2026.02월.260212.보물섬의 Docstring

L(육지) W(바다)
상하좌우 이웃 육지로만 가능, 한칸에 1시간.
보물까지 최단거리로 이동할 때, 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있음.

BFS 250번 치면 될것 같은 문제.
'''
from collections import deque

height, width = map(int, input().split())
grid = [input() for _ in range(height)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = 0

def inRange(x, y):
    return 0 <= x < height and 0 <= y < width

def BFS(x, y):
    global answer
    q = deque()
    visited = [[False for _ in range(width)] for _ in range(height)]
    visited[x][y] = True
    q.append((x, y, 0))
    while q:
        x, y, cnt = q.popleft()
        answer = max(answer, cnt)
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if inRange(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 'L':
                visited[nx][ny] = True
                q.append((nx, ny, cnt+1))

for x in range(height):
    for y in range(width):
        if grid[x][y] == 'L':
            # [최적화] 상하가 육지거나 좌우가 육지인 '중간 육지'는 패스
            if 0 < x < height - 1 and grid[x-1][y] == 'L' and grid[x+1][y] == 'L':
                continue
            if 0 < y < width - 1 and grid[x][y-1] == 'L' and grid[x][y+1] == 'L':
                continue
            BFS(x, y)
print(answer)