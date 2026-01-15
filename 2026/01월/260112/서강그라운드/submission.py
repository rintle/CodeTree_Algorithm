'''
260112.서강그라운드.submission의 Docstring
전형적인 최단거리 문제이기도 하고, BFS 문제이기도 한 것 같다.
BFS로 푸는 경우에는 BFS로 거리를 초과하지 않는 범위의 
아이템을 모두 더하면 될 것이다.
'''
from heapq import heappush, heappop
n, m, r = map(int, input().split())
items = [0]+list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

MAX_DIST = 16

def dijkstra(start):
    q = []
    distance = [MAX_DIST for _ in range(n+1)]
    distance[start] = 0
    heappush(q, (0, start))
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for d, e in graph[now]:
            cost = dist + d
            if distance[e] > cost:
                distance[e] = cost
                heappush(q, (cost, e))
    tmp = 0
    for i in range(n+1):
        if distance[i] <= m:
            tmp += items[i]
    return tmp


ans = 0
for i in range(1, n+1):
    ans = max(dijkstra(i), ans)
    # break
print(ans)