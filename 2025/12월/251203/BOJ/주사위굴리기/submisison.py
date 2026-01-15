dice = [0,0,0,0,0,0]
# 0 is top, 5 is bottom
N,M,x,y,K = map(int, input().split())

grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

comm = list(map(int, input().split()))

def roll(direction):
    global dice
    # east
    if direction == 1:
        # 2,5, 고정, 1,3,6,4 rotate
        dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    # west
    elif direction == 2:
        # 2,5, 고정, 1,3,6,4 rotate
        dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    # north
    elif direction == 3:
        # 4,3 고정, 2,1,5,6 rotate
        dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    elif direction == 4:
        dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]

def inRange(x, y):
    return 0<= x < N and 0 <= y < M

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

for com in comm:
    nx, ny = x+dx[com], y+dy[com]
    if inRange(nx, ny):
        roll(com)
        if grid[nx][ny] == 0:
            grid[nx][ny] = dice[5]
        else:
            dice[5] = grid[nx][ny]
            grid[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])