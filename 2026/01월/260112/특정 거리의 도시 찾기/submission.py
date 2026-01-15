'''
260112.특정 거리의 도시 찾기.submission의 Docstring
단순한 Dijkstra 문제.
X에서 거리가 K인 도시들의 번호를 출력하는 문제이다.
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INT_MAX = 300001
N, M, K, X = map(int, input().split())
dist = [INT_MAX for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

dist[X] = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    while q:
        d, cur = heappop(q)
        if dist[cur] < d:
            continue
        for i in graph[cur]:
            cost = d + 1
            if cost < dist[i]:
                dist[i] = cost
                heappush(q, (cost, i))
        # print(dist)
    cnt = 0
    for i in range(1, N+1):
        if dist[i] == K:
            print(i)
            cnt +=1
    if cnt == 0:
        print(-1)
dijkstra(X)