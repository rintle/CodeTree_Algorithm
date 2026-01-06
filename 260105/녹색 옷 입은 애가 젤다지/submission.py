'''
260105.녹색 옷 입은 애가 젤다지.submission의 Docstring
그래프 탐색 문제인 줄 알았으나, 잘못 생각함.
Dijkstra 문제임.
문제에서 알 수 있는 데
1. '최소 금액'
2. 시작과 끝이 정해져 있음.
'''

import heapq

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def inRange(x, y, N):
    return 0 <= x < N and 0 <= y < N
cnt = 1
ans = ''
while True:
    N = int(input())
    if N == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    MAX_rupee = N*N*9
    dist = [[MAX_rupee+1 for _ in range(N)] for _ in range(N)]

    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    while pq:
        rupee, x, y = heapq.heappop(pq)

        if rupee > dist[x][y]:
            continue

        if (x,y) == (N-1, N-1):
            break

        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if inRange(nx ,ny, N):
                new_rupee = rupee + grid[nx][ny]
                if new_rupee < dist[nx][ny]:
                    dist[nx][ny] = new_rupee
                    heapq.heappush(pq, (new_rupee, nx, ny))
    ans += f'Problem {cnt}: {dist[N-1][N-1]}\n'
    cnt += 1
print(ans)