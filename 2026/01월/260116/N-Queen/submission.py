'''
2026.01월.260116.N-Queen.submission의 Docstring
크기가 NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제.
배열을 숫자로 생각하고, 숫자를 뽑는다.
예)
N=6일 때
  0  1  2  3  4  5
  6  7  8  9 10 11
 12 13 14 15 16 17
 18 19 20 21 22 23
 24 25 26 27 28 29
 30 31 32 33 34 35
대각 : +- (N+1) / +-(N-1)
 
N=5일 때
  0  1  2  3  4
  5  6  7  8  9
 10 11 12 13 14
 15 16 17 18 19
 20 21 22 23 24

행: num//N
열: num%N

숫자를 뽑을 때, 뽑을 수 있는지 미리 조사한다.
인덱스 매핑인건 알고 있는데, 문제가 더 어렵다
'''
N = int(input())

used_col = [False for _ in range(N)]
used_diag1 = [False for _ in range(N*2)]
used_diag2 = [False for _ in range(N*2)]
ans = 0
def solve(row):
    global ans
    if row == N:
        ans += 1
        return
    for col in range(N):
        if not used_col[col] and not used_diag1[row+col] and not used_diag2[row-col+N-1]:
            used_col[col] = used_diag1[row+col] = used_diag2[row-col+N-1] = True
            solve(row+1)
            used_col[col] = used_diag1[row+col] = used_diag2[row-col+N-1] = False
solve(0)
print(ans)