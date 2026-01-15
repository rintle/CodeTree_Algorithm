'''
251210.BOJ.감시.submission의 Docstring
cctv의 개수가 8개를 넘지 않고
사무실의 크기도 최대 8x8인 것을 보았을 때,

1. backtracking을 사용해서 경우의 수 생성
2. simulation으로 감시 지역 update
3. 사각지대 크기 출력
4. backtracking의 return은 사각지대의 크기이며, return할 값들을 min으로 받는다.

순서로 진행하면 될 것 같다.
'''
from collections import deque
from copy import deepcopy
dx = [0,1,0,-1]
dy = [1,0,-1,0]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
CCTVs = []
for i in range(N):
    for j in range(M):
        if 1 <= grid[i][j] <= 5:
            CCTVs.append((grid[i][j], i, j))

directions = deque()

def inRange(x, y):
    return 0 <= x < N and 0 <= y < M


def simulate():
    new_grid = deepcopy(grid)
    for idx, cctv in enumerate(CCTVs):
        cctv_type, x, y = cctv
        if cctv_type == 1:
            d = directions[idx]
            nx, ny = x+dx[d], y+dy[d]
            while inRange(nx, ny) and new_grid[nx][ny] != 6:
                if new_grid[nx][ny] != 0:
                    nx, ny = nx+dx[d], ny+dy[d]
                else:
                    new_grid[nx][ny] = '#'
                    nx, ny = nx+dx[d], ny+dy[d]
        elif cctv_type == 2:
            d1, d2 = directions[idx], (directions[idx]+2) % 4
            nx, ny = x+dx[d1], y+dy[d1]
            while inRange(nx, ny) and new_grid[nx][ny] != 6:
                if new_grid[nx][ny] != 0:
                    nx, ny = nx+dx[d1], ny+dy[d1]
                else:
                    new_grid[nx][ny] = '#'
                    nx, ny = nx+dx[d1], ny+dy[d1]
            nx, ny = x+dx[d2], y+dy[d2]
            while inRange(nx, ny) and new_grid[nx][ny] != 6:
                if new_grid[nx][ny] != 0:
                    nx, ny = nx+dx[d2], ny+dy[d2]
                else:
                    new_grid[nx][ny] = '#'
                    nx, ny = nx+dx[d2], ny+dy[d2]
        elif cctv_type == 3:
            d1, d2 = directions[idx], (directions[idx]+1) % 4
            nx, ny = x+dx[d1], y+dy[d1]
            while inRange(nx, ny) and new_grid[nx][ny] != 6:
                if new_grid[nx][ny] != 0:
                    nx, ny = nx+dx[d1], ny+dy[d1]
                else:
                    new_grid[nx][ny] = '#'
                    nx, ny = nx+dx[d1], ny+dy[d1]
            nx, ny = x+dx[d2], y+dy[d2]
            while inRange(nx, ny) and new_grid[nx][ny] != 6:
                if new_grid[nx][ny] != 0:
                    nx, ny = nx+dx[d2], ny+dy[d2]
                else:
                    new_grid[nx][ny] = '#'
                    nx, ny = nx+dx[d2], ny+dy[d2]
        elif cctv_type == 4:
            d1, d2, d3 = directions[idx], (directions[idx]+1) % 4, (directions[idx]+2) % 4
            nx, ny = x+dx[d1], y+dy[d1]
            while inRange(nx, ny) and new_grid[nx][ny] != 6:
                if new_grid[nx][ny] != 0:
                    nx, ny = nx+dx[d1], ny+dy[d1]
                else:
                    new_grid[nx][ny] = '#'
                    nx, ny = nx+dx[d1], ny+dy[d1]
            nx, ny = x+dx[d2], y+dy[d2]
            while inRange(nx, ny) and new_grid[nx][ny] != 6:
                if new_grid[nx][ny] != 0:
                    nx, ny = nx+dx[d2], ny+dy[d2]
                else:
                    new_grid[nx][ny] = '#'
                    nx, ny = nx+dx[d2], ny+dy[d2]
            nx, ny = x+dx[d3], y+dy[d3]
            while inRange(nx, ny) and new_grid[nx][ny] != 6:
                if new_grid[nx][ny] != 0:
                    nx, ny = nx+dx[d3], ny+dy[d3]
                else:
                    new_grid[nx][ny] = '#'
                    nx, ny = nx+dx[d3], ny+dy[d3]
        elif cctv_type == 5:
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                while inRange(nx, ny) and new_grid[nx][ny] != 6:
                    if new_grid[nx][ny] != 0:
                        nx, ny = nx+dx[d], ny+dy[d]
                    else:
                        new_grid[nx][ny] = '#'
                        nx, ny = nx+dx[d], ny+dy[d]

    rlt = 0
    for g in new_grid:
        # print(*g)
        rlt += g.count(0)
    # print('='*20)
    return rlt

def backtrack(idx):
    global directions
    if idx == len(CCTVs):
        return simulate()
    
    rlt = 100
    # 5번 cctv는 4방향이기 때문에 1개만.
    if CCTVs[idx][0] == 5:
        directions.append(0)
        rlt = min(rlt, backtrack(idx+1))
        directions.pop()
    # 2번 cctv는 중복되는 부분이 있기 때문에 2개만.
    elif CCTVs[idx][0] == 2:
        for d in range(2):
            directions.append(d)
            rlt = min(rlt, backtrack(idx+1))
            directions.pop()
    else:
        for d in range(4):
            directions.append(d)
            rlt = min(rlt, backtrack(idx+1))
            directions.pop()

    return rlt

print(backtrack(0))