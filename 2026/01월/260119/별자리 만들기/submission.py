'''
2026.01월.260119.별자리 만들기.submission의 Docstring
N개의 별을 이어 별자리
1. 서로 다른 두 별을 일직선으로 이은 형태
2. 모든 별들이 이어져있어야함.

좌표들이 주어지니, edge를 내가 직접 만들어야 한다.
1. 먼저 Node에 좌표값을 다 저장하고
2. Edges에 거리를 구해 추가한다!
'''
import heapq
nodes = []
edges = []
n = int(input())
for _ in range(n):
    x, y = map(float, input().split())
    nodes.append((x, y))
for i in range(n):
    ix, iy = nodes[i]
    for j in range(i+1, n):
        jx, jy = nodes[j]
        dist = round(((ix-jx)**2+(iy-jy)**2)**.5, 2)
        heapq.heappush(edges, (dist, i, j))
root = [x for x in range(n)]
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

def is_cycle(x, y):
    return find(x)==find(y)
ans = 0
while edges:
    w, u, v = heapq.heappop(edges)
    if is_cycle(u, v):
        continue
    else:
        union(u, v)
        ans += w
print(ans)