'''
251231.어항 정리.submission의 Docstring
가정: 어항 안이 0이 될 수는 없다.
아마 문제 논리 상 0이 되기는 어렵다.
뺏겨도 최대 4*n개를 빼앗기게 될 텐데, n이 커지려면 그만큼 5배수만큼 차이가 나는 상황임.
4방향에서 1씩 빼앗긴다는 것은 각 주위의 어항 대비 5 이상씩 크다는 것이고, 즉 값은 1보다 작아질 수 없다.
'''

N, K = map(int, input().split())
MAX_VAL = 100
MAX_HEIGHT = 65
grid = [[0 for _ in range(MAX_VAL)] for _ in range(MAX_HEIGHT)]
bottom = 9
fishes = list(map(int, input().split()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(len(fishes)):
    grid[bottom][i] = fishes[i]

def printBowl(height=0):
    print('='*20)
    for i in range(bottom-height, N):
        print(*grid[i][:N])
    print('='*20)

def inRange(x, y):
    return 0 <= x < MAX_HEIGHT and 0 <= y < MAX_VAL

def moveFishes():
    global grid
    new_grid = [[0 for _ in range(MAX_VAL)] for _ in range(MAX_HEIGHT)]
    
    for i in range(MAX_HEIGHT):
        for j in range(MAX_VAL):
            if grid[i][j] != 0:
                x, y = i, j
                if not new_grid[x][y]:
                    fish_val = grid[x][y]
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if inRange(nx, ny) and grid[nx][ny]:
                            d = abs(grid[x][y] - grid[nx][ny]) // 5
                            if d > 0:
                                if grid[nx][ny] > grid[x][y]:
                                    fish_val += d
                                else:
                                    fish_val -= d
                    new_grid[x][y] = fish_val
    grid = new_grid

def allignBowl():
    global grid
    start = 0
    for i in range(N):
        if grid[bottom][i] != 0:
            # 위로 올라가면서 값 업데이트
            h = bottom
            f_list = []
            while grid[h][i]:
                f_list.append(grid[h][i])
                grid[h][i]=0
                h -= 1
            for f in f_list:
                grid[bottom][start] = f
                start += 1

def simulate1():
    # 최소 어항에 물고기 1마리 넣기
    min_val = 10001
    min_bowl = []
    for i in range(MAX_VAL):
        if grid[bottom][i] != 0:
            if min_val > grid[bottom][i]:
                min_val = grid[bottom][i]
                min_bowl = [i]
            elif min_val == grid[bottom][i]:
                min_bowl.append(i)
    for i in min_bowl:
        grid[bottom][i] += 1
    # 가장 왼쪽의 어항을 쌓기
    # height = 1
    grid[bottom - 1][1] = grid[bottom][0]
    grid[bottom][0] = 0
    start = 1
    # 높이가 2 이상 쌓인 어항들에 대해서 공중부양 -> 90도 회전 -> 쌓기 반복. 바닥이 있는 경우에만.
    while True:
        max_height = 0
        once=True
        rotate_idx = []
        prev_start = start
        for i in range(start,N):
            if grid[bottom - 1][i] != 0:
                rotate_idx.append(i)
                h = bottom
                if once:
                    while grid[h][i] != 0:
                        max_height+=1
                        h -= 1
                    once=False
            else:
                start = i
                break
        # max_height //= 2
        # printBowl(4)
        # print('max_height:', max_height)
        # print('start_idx:',start)
        # print('rotate_idx:',rotate_idx)
        # print('start + max_height:', start+max_height)
        # print('len_bowl:', N)
        if start+max_height > N or prev_start == start:
            break
        # 하나씩 쌓아 올리기 위해서 reverse
        height = 1
        rotate_idx.reverse()
        for idx in rotate_idx:
            cur_height = bottom
            cnt = 0
            while True:
                if grid[cur_height][idx] == 0:
                    break
                grid[bottom - height][start+cnt] = grid[cur_height][idx]
                grid[cur_height][idx] = 0
                cur_height -= 1
                cnt += 1
            height += 1
        # printBowl(2)
   
    # printBowl(4)
    # exit(0)
    # 물고기 이동
    moveFishes()
    

    # 어항 정상화
    allignBowl()

def simulate2():
    # 1번 접기
    start = N//2
    cnt = 1
    height = 1
    for i in range(start, N):
        grid[bottom-height][i] = grid[bottom][start-cnt]
        grid[bottom][start-cnt] = 0
        cnt += 1

    # 2번 접기
    start = N//2 + N//2//2
    cnt = 1
    for i in range(start, N):
        grid[bottom-2][i] = grid[bottom-1][start-cnt]
        grid[bottom-1][start-cnt] = 0
        cnt += 1

    cnt = 1
    for i in range(start, N):
        grid[bottom-3][i] = grid[bottom][start-cnt]
        grid[bottom][start-cnt] = 0
        cnt += 1
    
    moveFishes()

    allignBowl()
'''
8 7
5 2 3 14 9 2 11 8
'''
ans = 0
while True:
    max_val = max(grid[bottom])
    min_val = 10001
    for i in range(MAX_VAL):
        if grid[bottom][i] != 0:
            min_val = min(min_val, grid[bottom][i])
    diff = max_val - min_val
    if diff <= K:
        break

    simulate1()

    simulate2()
    ans += 1
# printBowl()
print(ans)