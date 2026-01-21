'''
2026.01월.260119.도시 분할 계획.submission의 Docstring
원숭이 한 마리가 세상 구경. 평화마을감.
N개의 집, M개의 길, 유지비 있음.
마을의 이장: 두개의 마을로 분리할 계획.
길이 너무 많아.
1. MST로 최소 비용을 갖는 트리를 구함
2. 가장 비싼 비용의 다리를 제거함
완성.
N : 2 ~ 100,000
M: 1 ~ 1,000,000
입력이 많으니, sys활용 (백준 특수)
'''
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    heapq.heappush(edges, (w, u, v))
root = [i for i in range(N+1)]
def find(x):
    if root[x] == x:
        return root[x]
    else:
        root[x] = find(root[x])
        return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    root[x] = y

def is_cycle(x,y):
    return find(x) == find(y)

max_price = -1
ans = 0
while edges:
    w, u, v = heapq.heappop(edges)
    if is_cycle(u,v):
        continue
    else:
        union(u, v)

        max_price = max(max_price, w)
        ans += w
print(ans-max_price)