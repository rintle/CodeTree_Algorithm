from collections import deque

N = int(input())
M = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

route = list(map(int, input().split()))
route = [r-1 for r in route]

# 각 도시에서 어떤 도시까지 갈 수 있는지를 기록해두자.
# BFS로 한번 훑고 지나가면, 연결된 모든 도시를 알 수 있다.
# 연결성을 확보했으면, 그대로 여행 계획이 가능한 지 체크하면 된다.
# grid[0][1] : 0->1까지 경로가 있다는 뜻
# dx dy가 아니고, row를 순회하며 다음 장소를 방문하면 된다.

visited = [False for _ in range(N)]

possible = [[False for _ in range(N)] for _ in range(N)]
def BFS(start):
    global possible, visited
    q = deque()
    q.append(start)
    visited[start] = True
    possible[start][start] = True
    while q:
        cur = q.popleft()
        for next in range(N):
            if grid[cur][next] and not visited[next]:
                q.append(next)
                visited[next]=True
                possible[start][next]=True
                possible[next][start]=True

# 시작 point
for s in range(N):
    visited = [False for _ in range(N)]
    BFS(s)

YES = True
for i in range(1, M):
    start = route[i-1]
    end = route[i]
    if possible[start][end]:
        continue
    else:
        YES = False
if YES:
    print("YES")
else:
    print("NO")