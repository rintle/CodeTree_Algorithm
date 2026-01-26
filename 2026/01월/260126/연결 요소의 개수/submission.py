'''
2026.01월.260126.연결 요소의 개수.submission의 Docstring
방향없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램.
연결 요소? 최대한 연결된 부분 집합을 의미한다.
모든 그래프가 하나로 연결되어 있으면 그 그래프는 연결 요소가 1개.
둘로 나눠진다면 연결요소가 2개.
'''
import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline
N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
# matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
visited[0] = True

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
#     matrix[u][v] = 1
#     matrix[v][u] = 1
def dfs(no):
    if visited[no]:
        return
    visited[no] = True
    for next in adj_list[no]:
        if not visited[next]:
            dfs(next)
# def dfs(no):
#     if visited[no]:
#         return
    
#     visited[no] = True
#     for v in range(1, N+1):
#         if matrix[no][v] and not visited[v]:
#             dfs(v)
ans = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)