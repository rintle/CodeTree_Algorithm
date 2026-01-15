from collections import deque
from copy import deepcopy
M, S = map(int, input().split())
fish = []
fdx = [0,-1,-1,-1,0,1,1,1]
fdy = [-1,-1,0,1,1,1,0,-1]
sdx = [0,-1,0,1,0]
sdy = [0,0,-1,0,1]
sent = [[0 for _ in range(4)] for _ in range(4)]
# sent[0][1]=sent[0][3]=sent[1][1]=sent[1][2]=sent[1][3] = 1
grid = [[deque() for _ in range(4)] for _ in range(4)]
move_ways = []
q = deque()
def permutation(cnt):
    if cnt > 2:
        move_ways.append(tuple(q))
        return
    for d in range(1,5):
        q.append(d)
        permutation(cnt+1)
        q.pop()
permutation(0)

for _ in range(M):
    x, y, d = map(int, input().split())
    grid[x-1][y-1].append(d-1)
shark_x, shark_y = map(int, input().split())
shark_x, shark_y = shark_x-1, shark_y-1
def printG():
    print('='*20)
    print('shark')
    for i in range(4):
        for j in range(4):
            if (i,j) == (shark_x, shark_y):
                print('@', end='')
            else:
                print('.', end='')
        print()
    print('-'*20)
    for s in sent:
        print(*s)
    for g in grid:
        print(*g)
    print('='*20)

def inRange(x, y):
    return 0<=x<4 and 0<=y<4

def canFishGo(x, y):
    return inRange(x, y) and (x, y) != (shark_x, shark_y) and sent[x][y] == 0

def moveFish():
    global grid
    new_grid = [[deque() for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            # 물고기가 있는 경우, loop를 돈다
            while grid[x][y]:
                d = grid[x][y].popleft()
                fish_move=False
                for i in range(8):
                    nd = (d-i)%8
                    nx, ny = x+fdx[nd], y+fdy[nd]
                    if canFishGo(nx, ny):
                        new_grid[nx][ny].append(nd)
                        fish_move=True
                        break
                if not fish_move:
                    new_grid[x][y].append(d)
    grid = new_grid
    # print('fish move to')
    # for g in new_grid:
    #     print(*g)
    # print('-'*20)

def moveShark():
    global shark_x, shark_y
    max_fish = -1
    max_path = None
    for path in move_ways:
        visited = [[False for _ in range(4)] for _ in range(4)]
        x, y = shark_x, shark_y
        cnt = 0
        fail = False
        for d in path:
            nx, ny = x+sdx[d], y+sdy[d]
            if inRange(nx, ny):
                if not visited[nx][ny]:
                    cnt += len(grid[nx][ny])
                x, y = nx, ny
                visited[nx][ny] = True
            else:
                fail=True
                break
        if not fail:
            if max_fish < cnt:
                max_fish = cnt
                max_path = path
    
    for d in max_path:
        shark_x, shark_y = shark_x+sdx[d], shark_y+sdy[d]
        if grid[shark_x][shark_y]:
            sent[shark_x][shark_y] = 3
            grid[shark_x][shark_y] = deque()

'''
 ↑, ←, ↓, →
 1  2  3  4
'''
def sentDown():
    for x in range(4):
        for y in range(4):
            if sent[x][y]:
                sent[x][y] -= 1
'''
 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
 0   1  2  3   4  5   6  7
'''
def simulate():
    # copy
    copy_fish = deepcopy(grid)
    # fish move
    moveFish()

    # shark move
    moveShark()
    
    # print('shark move to')
    # for i in range(4):
    #     for j in range(4):
    #         if (i,j) == (shark_x, shark_y):
    #             print('@', end='')
    #         else:
    #             print('.', end='')
    #     print()
    # print('-'*20)
    # sent -1
    sentDown()

    # for s in sent:
    #     print(*s)
    # print('-'*20)
    # paste fish
    for x in range(4):
        for y in range(4):
            while copy_fish[x][y]:
                grid[x][y].append(copy_fish[x][y].popleft())
#     print('final fish')
#     for g in grid:
#         print(*g)
# printG()
# print('#'*50)
for _ in range(S):
    simulate()
    # print('#'*50)
    # breakpoint()
    # printG()
    
ans = 0
for x in range(4):
    for y in range(4):
        ans+=len(grid[x][y])
print(ans)