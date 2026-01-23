'''
2026.01월.260123.플로이드.submission의 Docstring
n개의 도시. m개의 버스.
n과 m이 주어짐.
'''
import sys
n = int(input())
m = int(input())
INT_MAX = sys.maxsize
grid = [[INT_MAX for _ in range(n)] for _ in range(n)]
for i in range(n):
    grid[i][i] = 0

for _ in range(m):
    x, y, w = map(int, input().split())
    x -= 1
    y -= 1
    grid[x][y] = min(w, grid[x][y])
    
for k in range(n):
    for x in range(n):
        for y in range(n):
            grid[x][y] = min(grid[x][y], grid[x][k]+grid[k][y])

for g in grid:
    for price in g:
        if price == INT_MAX:
            print('0', end=' ')
        else:
            print(price, end=' ')
    print()