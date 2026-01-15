'''
2026.01월.260115.도영이가 만든 맛있는 음식.submission2의 Docstring
비트마스킹으로 풀이하기
'''
import sys
N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]
min_diff = sys.maxsize
for c in range(1, (1<<N)):
    s = 1
    b = 0

    for j in range(N):
        if (c >> j) & 1:
            s *= ingredients[j][0]
            b += ingredients[j][1]
    
    min_diff = min(min_diff, abs(s-b))
print(min_diff)