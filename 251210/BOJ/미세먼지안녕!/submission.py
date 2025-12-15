R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

# aircon[0] : top
# aircon[1] : bottom
aircon = []
for i in range(R):
    for j in range(C):
        if grid[i][j] == -1:
            aircon.append((i,j))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
#     → ↓  ← ↑  
def inRange(x, y):
    return 0 <= x < R and 0 <= y < C

def diffuse():
    global grid
    new_grid = [[0 for _ in range(C)] for _ in range(R)]
    for ac in aircon:
        x, y = ac
        new_grid[x][y] = -1
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                # 확산 시작
                remain = grid[i][j]
                spread = remain//5
                for d in range(4):
                    nx, ny = i+dx[d], j+dy[d]
                    if inRange(nx, ny) and grid[nx][ny] != -1:
                        new_grid[nx][ny] += spread
                        remain -= spread
                new_grid[i][j] += remain
    grid = new_grid   

def activate():
    global grid
    direction_list = [[3,0,1,2], [1,0,3,2]]
    # top
    x, y = aircon[0]
    directions = [3,0,1,2]
    for d in directions:
        nx, ny = x+dx[d], y+dy[d]
        # print(f'nx, ny: {nx, ny}')
        # print(f'aircon\'s y: {aircon[0][1]}')
        while inRange(nx,ny) and nx <= aircon[0][0]:
            if grid[x][y] != -1 and grid[nx][ny] != -1:
                grid[x][y] = grid[nx][ny]
            elif grid[nx][ny] == -1:
                grid[x][y]=0
            x,y = nx, ny
            nx, ny = x+dx[d], y+dy[d]

    # bottom
    x, y = aircon[1]
    directions = [1,0,3,2]
    for d in directions:
        nx, ny = x+dx[d], y+dy[d]
        # print(f'nx, ny: {nx, ny}')
        # print(f'aircon\'s y: {aircon[0][1]}')
        while inRange(nx,ny) and nx >= aircon[1][0]:
            if grid[x][y] != -1 and grid[nx][ny] != -1:
                grid[x][y] = grid[nx][ny]
            elif grid[nx][ny] == -1:
                grid[x][y]=0
            x,y = nx, ny
            nx, ny = x+dx[d], y+dy[d]
    '''
5 3 1
10 0 0
 0 30  7
-1 10  0
-1  0 20
0 0 0
    '''
    # directions = [3,0,1,2]
    # x, y = aircon[0]

    # # bottom
    # directions = [1,0,3,2]
    # x, y = aircon[1]
    pass

while T:
    diffuse()
    activate()
    T -= 1
ans = 2
for g in grid:
    ans += sum(g)
print(ans)
'''
3 3 1
0 0 0
0 46 0
0 0 0

4 3 1
 0 30  7
-1 10  0
-1  0 20
0 0 0

30 확산 (3방향 확산)
30-18=12
 6 12  6
    6  0
    0  0

7 확산 (2방향 확산)
 0  1  5
    0  1

10 확산(3방향 확산)
 0  2  0
    4  2
    2

20 확산(2방향 확산)
 0  0  0
    0  4
    4 12

확산 이후 값을 더해보면...
 6 15 11
   10  7
    6 12
좋아쓰
'''