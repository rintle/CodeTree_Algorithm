'''
2026.01월.260121.아기 상어.submission의 Docstring
NxN에 물고기 M마리, 아기상어 1마리.
한칸에 최대 물고기 한마리
크기는 자연수. 처음에 아기 상어는 2, 아기상어는 1초에 상하좌우 이동 가능
이동조건:
1. 아기상어는 지보다 큰거 못지나감.
2. 지보다 작은 물고기는 먹음
3. 같은 크기의 물고기는 못먹지만 지나갈 수 잇음

이동 결정 조건
1. 먹을 수 있는 물고기가 없다면 - 엄마에게 도움 요청 (순회 종료)
(사실상 2, 3은 BFS해서 먼저 나오는 걸로 가서 먹으면 됨)
2. 먹을 수 있는 물고기가 1마리라면 - 그 물고기 먹으러 감
3. 먹을 수 있는 물고기가 1마리 이상이라면 - 가장 가까운 물고기
    3-1. 가까운 거리 : 칸 개수의 최소값(맨허튼 거리)
    3-2. 가까운 거리가 많다면, 가장 위의 물고기 가장 왼쪽 물고기 순서(dx,dy 순서 알려주는거임)
    dx, dy 순서 알려주는건 내 착각이었음. 먹을 수 있는 최소 거리 물고기를 다 뽑아놓고, 3-2 순서에 맞는거를 먹는거가 맞다.
이동 1초, 먹는 시간 없음. 이동과 동시에 물고기 먹음. 먹으면 빈칸.
크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가함.
'''
from collections import deque
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
shark = (0, 0)
shark_size = 2
shark_ate = 0
time = 0
for x in range(N):
    for y in range(N):
        if grid[x][y] == 9:
            shark = (x, y)
            grid[x][y] = 0
dx = [-1,0,0,1]
dy = [0,-1,1,0]

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

def findFish():
    max_dist = 20*20
    fish_loc = (0, 0)
    visited = [[False for _ in range(N)] for _ in range(N)]
    eatlist = [[False for _ in range(N)] for _ in range(N)]
    q = deque()
    x, y = shark
    q.append((x, y, 0))
    visited[x][y] = True
    while q:
        x, y, dist = q.popleft()
        if dist >= max_dist:
            continue
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if inRange(nx, ny) and not visited[nx][ny] and grid[nx][ny] <= shark_size:
                if grid[nx][ny] == 0 or grid[nx][ny] == shark_size:
                    q.append((nx, ny, dist+1))
                    visited[nx][ny] = True
                else:
                    max_dist = dist+1
                    eatlist[nx][ny] = True
                    # return (nx, ny, dist+1)
    for x in range(N):
        for y in range(N):
            if eatlist[x][y]:
                return (x, y, max_dist)
    return False


while True:
    result = findFish()
    if result:
        x, y, dist = result
        shark = (x, y)
        time += dist
        shark_ate += 1
        grid[x][y] = 0
        if shark_size == shark_ate:
            shark_size += 1
            shark_ate = 0
    else:
        break
print(time)