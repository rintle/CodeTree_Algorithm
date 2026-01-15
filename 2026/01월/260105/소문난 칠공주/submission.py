'''
260105.소문난 칠공주.submission의 Docstring
백트래킹과 BFS를 조합하면 될 것 같음
'''
from collections import deque
N = 5
grid = [list(input()) for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(arr):
    visited = [[True for _ in range(N)] for _ in range(N)]
    for(x, y) in arr:
        visited[x][y] = False
    q = deque()
    q.append(arr[0])
    x, y = arr[0]
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    if cnt == 7:
        return True
    return False

def pick_seven(depth, start, cnt):
    global result
    if cnt >= 4:
        return
    if depth == 7:
        if bfs(arr):
            result += 1
    for i in range(start, 25):
        r, c = i//N, i%N
        arr.append((r,c))
        pick_seven(depth+1, i+1, cnt + (grid[r][c]=='Y'))
        arr.pop()

arr = []
result = 0
pick_seven(0,0,0)
print(result)