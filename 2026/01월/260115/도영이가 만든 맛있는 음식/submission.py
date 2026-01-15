'''
2026.01월.260115.도영이가 만든 맛있는 음식.submission의 Docstring
N개의 재료가 있음.
각 재료의 신맛 S와 쓴맛 B를 알고 있음.
음식의 신맛 : 사용한 재료의 신맛의 곱
음식의 쓴맛 : 사용한 재료의 쓴맛의 합

차이를 작게 만들고자 함. 재료는 최소 1개 사용해야함.
'''
import sys
INT_MAX = sys.maxsize
N = int(input())
visited = [False for _ in range(N)]

def findIng(idx):
    if idx == N:
        s, b = 1, 0
        choosen = False
        for i in range(N):
            if visited[i]:
                s *= ingredients[i][0]
                b += ingredients[i][1]
                choosen = True
        if choosen:
            return abs(s-b)
        else:
            return INT_MAX
    tmp = INT_MAX
    for i in range(idx, N):
        visited[i] = True
        tmp = min(tmp, findIng(i+1))
        visited[i] = False
        tmp = min(tmp, findIng(i+1))
    return tmp
ingredients = []
for _ in range(N):
    ingredients.append(tuple(map(int, input().split())))
if N == 1:
    print(abs(ingredients[0][0] - ingredients[0][1]))
else:
    print(findIng(0))