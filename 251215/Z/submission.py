'''
251215.Z.submission의 Docstring
모든 숫자를 순회할 필요는 없고,
찾고자 하는 r, c가
현재 어떤 사분면에 위치하고 있는지를 파악하고,
그만큼 숫자를 더해서 count하면 된다.
예) 
2 3 1
에서, N=2기에 4x4다.
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
처음에 이렇게 있을 떄, r, c는 3,1이다.
3,1의 위치는
0 0 0 0
0 0 0 0
0 v 0 0 
0 0 0 0
(편의상,
1 1 2 2
1 1 2 2
3 3 4 4 
3 3 4 4
위처럼 사분면을 구분짓는다.
)
여기므로, 3사분면에 위치한다.
그러면 3사분면(정사각형)에 대해서 다시 z를 계산하되,
시작 숫자는 2*2=8부터 시작하면 된다!
2(size//2) x 2(본인이 포함되는 사분면 - 1)
언제까지 반복하냐면, 함수에 들어오는 size가 1가 될 때까지 반복한다.
'''
N, r, c = map(int, input().split())

def findZ(x, y, size, cnt):
    if size == 2:
        grid = [[0 for _ in range(2)] for _ in range(2)]
        for i in range(2):
            for j in range(2):
                grid[i][j] = cnt
                cnt += 1
        # print(r, c, x, y)
        return grid[r-x][c-y]
    else:
        # check r,c in q1
        if x <= r < x + size//2 and y <= c < y + size//2:
            # print("To Q1")
            return findZ(x, y, size//2, cnt)
        # check r,c in q2:
        if x <= r < x + size//2 and y + size//2 <= c < y + size:
            # print("To Q2")
            return findZ(x, y + size//2, size//2, cnt+((size//2)*(size//2)))
        # check r,c in q3:
        if x + size//2 <= r < x + size and y <= c < y + size//2:
            # print("To Q3")
            return findZ(x+ size//2, y, size//2, cnt+((size//2)*(size//2)*2))
        # check r,c in q2:
        if x + size//2 <= r < x + size and y + size//2 <= c < y + size:
            # print("To Q4")
            return findZ(x+ size//2, y + size//2, size//2, cnt+((size//2)*(size//2)*3))
print(findZ(0,0,2**N,0))