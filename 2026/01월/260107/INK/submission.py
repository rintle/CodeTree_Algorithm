'''
260107.INK.submission의 Docstring
시뮬레이션 잘 맞춰서 진행하는 문제.
점프할 때, 맨허튼 거리 만큼 잉크가 칠해진다.
액션 함수
  - 이동
  - 충전
  - 점프
잉크 칠하는 함수
'''
I, N, K = map(int, input().split())
inks = list(input())
grid = [list(input()) for _ in range(N)]
commands = list(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
charged_ink = 0
ink_idx = -1
def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

move_table = {
    'U':3,
    'D':1,
    'L':2,
    'R':0
}

def move(x, y, comm):
    d = move_table[comm]
    nx, ny = x+dx[d], y+dy[d]
    if inRange(nx, ny) and grid[nx][ny] == '.':
        grid[x][y], grid[nx][ny] = '.', '@'

        return nx, ny
    return x, y

def jump(x, y):
    global ink_idx, charged_ink
    ink_idx = (ink_idx+1) % I
    for i in range(N):
        for j in range(N):
            m_dist = abs(x-i)+abs(y-j)
            if m_dist <= charged_ink and grid[i][j] !='.' and grid[i][j] != '@':
                grid[i][j] = inks[ink_idx]
    charged_ink = 0
def findBox():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '@':
                return i, j
x, y = findBox()
for c in commands:
    if c =='j':
        charged_ink += 1
    elif c == 'J':
        jump(x, y)
    else:
        x, y = move(x, y, c)

for g in grid:
    print(''.join(g))