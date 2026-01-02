'''
251231.스도쿠.submission의 Docstring
1. 현재 위치에서 3x3그리드의 어디에 속해있는지 확인해야 한다.
1-1. 확인한 이후, 가능한 숫자를 제외한다.
2. 현재 x열에 가능한 숫자를 제외한다.
3. 현재 y열에 가능한 숫자를 제외한다.
매 숫자를 넣기 전에, 가능한지 조사를 하게 되면 경우의 수가 너무 많아진다.
숫자를 넣기 전에, 가능한 숫자 list를 찾아내고, 그 안에서 값을 넣는 것이 현명하다.
9x9를 다 순회하는 것은 시간 낭비. 빈 공간들에 대해서만 쏙쏙 골라내어 값을 채우자.
'''
boundary = []
for i in range(0, 9, 3):
    tmp = []
    for j in range(0, 9, 3):
        tmp.append((i,j))
    boundary.append(tmp)

missing = []
grid = [list(map(int, list(input()))) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            missing.append((i, j))

# print(missing)
# for g in grid:
#     print(*g)
# for gs in boundary:
#     print(*gs)
# x, y = 5,5
# print((x)//3, (y)//3)
# print(boundary[(x)//3][(y)//3])

def findCandidates(x, y):
    includes = set()
    # 3x3 서칭
    x_top, y_top = boundary[x//3][y//3]
    # print(f"xtop, ytop: {x_top, y_top}")
    for i in range(x_top, x_top+3):
        for j in range(y_top, y_top+3):
            if grid[i][j] != 0:
                includes.add(grid[i][j])
        #     print(grid[i][j], end=' ')
        # print()

    # 종, 횡 서칭
    for i in range(9):
        if grid[x][i] != 0:
            includes.add(grid[x][i])
        if grid[i][y] != 0:
            includes.add(grid[i][y])
    r_list = []
    for n in range(1, 10):
        if n not in includes:
            r_list.append(n)
    return r_list

def fillMissing(idx):
    # if found answer
    if idx >= len(missing):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end='')
            print()
        exit(0)
    x, y = missing[idx]
    candidates = findCandidates(x, y)
    # print(x,y)
    # print(candidates)
    for candidate in candidates:
        grid[x][y] = candidate
        fillMissing(idx+1)
        grid[x][y] = 0

fillMissing(0)

# for g in grid:
#     print(*g)