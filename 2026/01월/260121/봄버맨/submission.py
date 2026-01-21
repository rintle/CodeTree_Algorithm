'''
2026.01월.260121.봄버맨.submission의 Docstring
RxC인 격자판 위에서 살고 있음
폭탄은 3초뒤 폭탄, 폴발 후 폭탄이 있던 칸 + 인접 4칸 파괴
폭탄 범위에 폭탄이 있다면, 폭탄은 폭발 없이 파괴 (연쇄 없음)
봄버맨 폭탄 면역

1. 봄버맨이 일부 칸에 폭탄 설치(설치 시간 동일)
2. 1초간 봄버맨 아무것도 안함
3. 폭탄이설치되지 않은 모든 칸에 폭탄 설치
4. 1 때 설치한 폭탄 모두 폭발
    3, 4 반복


폭탄의 경우 visited 말고 3, 2, 1 로 표현하면 될 듯
설치 시:
 폭탄 : 3
1초뒤 (아무것도 안함)
 폭탄 : 2 
2초뒤 (폭탄 미설치 칸에 모든 폭탄 설치)
 폭탄 : 1, 3
3초뒤 (폭발)
 폭탄 : x, 2
4초뒤 : (폭탄 미설치 칸에 모든 폭탄 설치)
 폭탄 : x, 1, 3
5초뒤 (폭발)
 폭탄 : x, x, 2
6초뒤 : (폭탄 미설치 칸에 모든 폭탄 설치)
 폭탄 : x, x, 1, 3
(3초 이후에는 계속 폭발 설치 폭발 설치 반복됨.)

반복.
'''
R, C, N = map(int, input().split())
grid = [[0 for _ in range(C)] for _ in range(R)]
explode = [[False for _ in range(C)] for _ in range(R)]
# def simulate():
# initial bomb
for r in range(R):
    tmp = list(input())
    for c in range(C):
        if tmp[c] == 'O':
            grid[r][c] = 3
# 아무것도 안하고 1초 지나기
for r in range(R):
    for c in range(C):
        if grid[r][c]:
            grid[r][c] -= 1
cnt = 1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def inRange(x, y):
    return 0 <= x < R and 0 <= y < C

def simulate(comm):
    # 짝수 : 폭탄 미설치 칸에 폭탄 설치
    if comm % 2 == 0:
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    grid[r][c] -= 1
                else:
                    grid[r][c] = 3
    else:
        # 폭탄 타이머 1씩 줄이고, 터지는 폭탄 및 범위 기록
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    explode[r][c] = True
                    for d in range(4):
                        nr, nc = r+dx[d], c+dy[d]
                        if inRange(nr, nc):
                            explode[nr][nc] = True
                else:
                    grid[r][c] -= 1
        # 기록 기반 업데이트
        for r in range(R):
            for c in range(C):
                if explode[r][c]:
                    explode[r][c] = False
                    grid[r][c] = 0
        
while cnt < N:
    cnt += 1
    simulate(cnt)
for r in range(R):
    for c in range(C):
        if grid[r][c]:
            print('O', end='')
        else:
            print('.', end='')
    print()