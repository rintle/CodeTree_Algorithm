'''
2026.01월.260123.n단 논법.submission의 Docstring
모든 중앙대 컴공 학생들은 미인이다.
지무근은 중앙대 컴공 학생이다.
지무근은 미인이다.
'''
n = int(input())
grid = [[False for _ in range(27)] for _ in range(27)]
for _ in range(n):
    x, _, y = input().split()
    x = ord(x)-ord('a')
    y = ord(y)-ord('a')
    grid[x][y] = True

for k in range(27):
    for x in range(27):
        for y in range(27):
            grid[x][y] = grid[x][y] or (grid[x][k] and grid[k][y])

m = int(input())
for _ in range(m):
    x, _, y = input().split()
    x = ord(x)-ord('a')
    y = ord(y)-ord('a')
    if grid[x][y]:
        print('T')
    else:
        print('F')