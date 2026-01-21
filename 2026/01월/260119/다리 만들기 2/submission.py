'''
2026.01월.260119.다리 만들기 2.submission의 Docstring
다리의 양 끝은 섬과 인접한 바다, 다리의 방향이 바뀌면 안됨. 길이는 2 이상.
어려워 보이는 문제는 아닌것 같음.
1. 섬들을 네이밍함. (1~N)
2. 격자에서 모든 다리를 먼저 구하기 with distance
3. MST let's go
4. MST로 만들어진 edges 개수가 N-1개 이하라면, -1(모든 섬 연결 불가)
'''
from collections import deque
import heapq
N, M = map(int, input().split())
grid = [list(map(int, input().split()))for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def inRange(x, y):
    return 0<=x<N and 0<=y<M

def bfs(x, y, cnt):
    global grid
    q = deque()
    q.append((x, y))
    grid[x][y] += cnt
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if inRange(nx,ny) and not visited[nx][ny] and grid[nx][ny]:
                q.append((nx, ny))
                grid[nx][ny] += cnt
                visited[nx][ny] = True
cnt = 0
islands = [0]
edges = []
for i in range(N):
    for j in range(M):
        if grid[i][j] and not visited[i][j]:
            bfs(i,j,cnt)
            islands.append((i,j))
            cnt += 1
# 인접 행렬 만들기 (섬 개수 최대 6개)
matrix = [[200 for _ in range(7)] for _ in range(7)]

for x in range(N):
    for y in range(M):
        if grid[x][y]:
            source = grid[x][y]
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                dist = 0
                target = None
                while inRange(nx, ny):
                    if grid[nx][ny]:
                        if dist <= 1:
                            break
                        else:
                            target = grid[nx][ny]
                            break
                    nx, ny = nx+dx[d], ny+dy[d]
                    dist += 1
                if target:
                    matrix[source][target] = min(matrix[source][target], dist)
             
for s in range(1, cnt+1):
    for d in range(s, cnt+1):
        if matrix[s][d] != 200:
            heapq.heappush(edges, (matrix[s][d], s, d))
root = [i for i in range(7)]
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

edge_cnt = 0
ans = 0
while edges:
    w, u, v = heapq.heappop(edges)
    if is_cycle(u,v):
        continue
    else:
        union(u, v)
        ans += w
        edge_cnt += 1
if edge_cnt != cnt-1:
    print(-1)
else:
    print(ans)