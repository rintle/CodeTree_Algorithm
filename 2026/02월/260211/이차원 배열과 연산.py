'''
2026.02월.260211.이차원 배열과 연산의 Docstring
크기가 3X3
인덱스 1부터 시작. 1초 지날때 마다 연산 적용됨.
R연산: 배열 A의 모든 행에 대해서 정렬 수행
    행의 개수 >= 열의 개수 인 경우에 적용
C연산: 배열 A의 모든 열에 대해서 정렬 수행
    행의 개수 < 열의 개수 인 경우에 적용

한 행/열에 있는 수를 정렬하면, 각 수가 몇번 나왔는지 알아야 한다.
수의 등장 횟수가 커지는 순(오름차순), 수가 커지는 순서대로 다시 정렬해 넣어야함.
배열에 넣을 때는 수와 등장 횟수를 모두 넣고, 순서는 수가 먼저.

[3, 1, 1] 정렬 -> [3, 1, 1, 2] 또 정렬 -> [2, 1, 3, 1, 1, 2]
R 연산이 진행되면 모든 행의 크기가 변함.
C 연산이 진행되면 모든 열의 크기가 변함.
크진 곳에는 0을 써야하고, 수를 정렬할 때 0은 무시해야함.

크기가 100을 넘어가면 처음 100개를 제외한 나머지는 버림.
배열 A에 들어있는 수와, r, c, k가 주어졌을 때 A[r][c]에 값이 k가 되기 위한 최소 시간
'''
import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()
matrix = [[0 for _ in range(100)] for _ in range(100)]

r, c, k = map(int, input().split())
r, c = r-1, c-1

for x in range(3):
    row = list(map(int, input().split()))
    for y in range(3):
        matrix[x][y] = row[y]
row, col = 3, 3
time = 0

def sortRow():
    global col
    # 먼저 훑어가며, 숫자를 counting
    # dict를 활용하면 좋을 것 같음.
    sorted_items = []
    for x in range(row):
        nums = defaultdict(int)
        for y in range(col):
            num = matrix[x][y]
            if num == 0:
                continue
            nums[num] += 1
        sorted_nums = sorted(nums.items(), key=lambda x: (x[1], x[0]))

        sorted_items.append([x for t in sorted_nums for x in t])
    new_col = max(len(sub) for sub in sorted_items)
    for r in range(row):
        for c in range(100):
            try:
                matrix[r][c] = sorted_items[r][c]
            except:
                matrix[r][c] = 0
    col = new_col

def sortCol():
    global row
    sorted_items = []
    for y in range(col):
        nums = defaultdict(int)
        for x in range(row):
            num = matrix[x][y]
            if num == 0:
                continue
            nums[num] += 1
        sorted_nums = sorted(nums.items(), key=lambda x: (x[1], x[0]))

        sorted_items.append([x for t in sorted_nums for x in t])
    new_row = max(len(sub) for sub in sorted_items)
    for c in range(col):
        for r in range(100):
            try:
                matrix[r][c] = sorted_items[c][r]
            except:
                matrix[r][c] = 0
    row = new_row
    

while matrix[r][c] != k and time <= 100:
    if row >= col:
        sortRow()
    else:
        sortCol()
    time += 1
    
if time > 100:
    print(-1)
else:
    print(time)