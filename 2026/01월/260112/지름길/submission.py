'''
260112.지름길.submission의 Docstring
DP로도 풀 수 있는 문제 같긴 하지만, Dijkstra Day기 때문에 Dijkstra로 풀었다.
'''
N, D = map(int, input().split())
graph={}
for _ in range(N):
    s, e, d = map(int, input().split())
    try:
        graph[s].append((e, d))
    except:
        graph[s] = [(e, d)]
dist = [i for i in range(D+1)]
for s in range(D+1):
    try:
        if s != 0:
            if dist[s] > dist[s-1]+1:
                dist[s] = dist[s-1]+1
        
        for e, d in graph[s]:
            if dist[s] + d < dist[e]:
                dist[e] = dist[s]+d
    except:
        pass
print(dist[D])