"""
2026.01월.260126.점프왕 쩰리 (Small).submission의 Docstring
1. 정사각형 내부에서만 움직임. 나가면 바로 게임오버
2. 출발점은 정사각형의 가장 왼쪽 위칸.
3. 오른쪽과 아래로만 이동 가능.
4. 오른쪽 아래칸에 도달하면 승리.
5. 쩰리가 한번에 이동할 수 있는 칸의 수는 현재 밟고 있는 칸의 수. 딱 그 수만큼 이동 가능.
"""
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)]for _ in range(N)]
dx = [0,1]
dy = [1,0]

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

def dfs(x, y):
    global visited
    if not inRange(x, y):
        return False
    if grid[x][y] == -1:
        return True
    if visited[x][y]:
        return False
    visited[x][y] = True
    return_val = False
    power = grid[x][y]
    for d in range(2):
        nx, ny = x+dx[d]*power, y+dy[d]*power
        return_val = dfs(nx, ny) or return_val
    return return_val
if dfs(0,0):
    print("HaruHaru")
else:
    print("Hing")