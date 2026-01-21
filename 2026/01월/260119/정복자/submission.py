'''
2026.01월.260119.정복자.submission의 Docstring
N개의 도시와 M개의 도로
양방향 도로, 필요 비용 존재. 
도시는 1번부터 N번까지 번호 붙여져있음
1번 도시만 점거하고 있음. 
도시 B를 점거하려면, B와 연결된 도시중 적어도 하나를 정복하고 있어야함.
1. MST를 구해서 도로 비용을 합산한다.
2. 사용한 도로 개수 -1만큼 t를 곱해 더한다.
N < 10000, M < 30000
입력을 받는게 좋겠네

Kruskal MST를 썼는데, 이건 틀렸다.
이유 : 문제에서도 알다시피, 1번부터 시작해야함.
Prim MST를 사용하자.
'''
import heapq
import sys
input = sys.stdin.readline
N, M, t = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(edges, (C, A, B))
parents = [i for i in range(N+1)]

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    parents[x] = y

def is_cycle(x, y):
    x = find(x)
    y = find(y)
    return x == y
ans = 0
cnt = 0
while edges:
    w, u, v = heapq.heappop(edges)
    if is_cycle(u, v):
        continue
    else:
        union(u, v)
        ans += w+cnt*t
        cnt += 1
print(ans)