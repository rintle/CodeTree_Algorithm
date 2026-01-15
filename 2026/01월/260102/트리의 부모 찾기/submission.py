from collections import deque
nodes = [[] for _ in range(100001)]
visited = [False for _ in range(100001)]
parents = [0 for _ in range(100001)]
N = int(input())
for _ in range(N-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
q = deque()
q.append(1)
visited[1] = True
parents[1] = 1
while q:
    p = q.popleft()
    for n in nodes[p]:
        if not visited[n]:
            parents[n] = p
            visited[n] = True
            q.append(n)
for i in range(2, N+1):
    print(parents[i])