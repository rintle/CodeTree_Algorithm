N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]
def printC():
    print('='*30)
    gd = [['.' for _ in range(N)] for _ in range(N)]
    for x,y in cloud:
        gd[x][y] ='#'
    for g in gd:
        print(*g)

def move(d, s):
    for i in range(len(cloud)):
        x, y = cloud[i]
        nx, ny = (x+dx[d]*s)%N, (y+dy[d]*s)%N
        cloud[i] = [nx, ny]

def inRange(x, y):
    return 0<=x<N and 0<=y<N

def bug():
    for x,y in cloud:
        for d in [2,4,6,8]:
            nx, ny = x+dx[d], y+dy[d]
            if inRange(nx, ny) and A[nx][ny]:
                A[x][y] += 1

def simulate():
    global cloud
    cloud_pos = [[False for _ in range(N)] for _ in range(N)]
    # global cloud
    d, s = map(int, input().split())
    move(d, s)
    for x, y in cloud:
        A[x][y] += 1
        cloud_pos[x][y] = True
    bug()
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and not cloud_pos[i][j]:
                new_cloud.append([i,j])
                A[i][j] -=2
    cloud = new_cloud
for _ in range(M):
    simulate()

ans = 0
for a in A:
    ans += sum(a)
print(ans)