'''
260112.최단경로.submission의 Docstring
확실히 Dijkstra문제이고, 시간제한이 1초로 빡빡하기 때문에 heapq를 사용해야할 것
입력도 꽤 많이 필요할 것 같아서,
'''
import sys
import heapq
input = sys.stdin.readline
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
start = int(input())
INF = sys.maxsize
distance = [INF for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for w, v in graph[cur]:
            cost = dist + w
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
    ans = []
    for i in distance[1:]:
        if i == INF:
            ans.append('INF')
        else:
            ans.append(str(i))
    print('\n'.join(ans))
dijkstra(start)