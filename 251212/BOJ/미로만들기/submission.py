from collections import deque

N = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

if N == 1:
    print(0)
else:
    grid = [list(map(int, list(input()))) for _ in range(N)]
    break_grid = [[N*N for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((0, 0,0))
    break_grid[0][0] = 0
    while q:
        x, y, cnt = q.popleft()
        b_cnt = break_grid[x][y]

        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if inRange(nx, ny):
                
                # is white room
                if grid[nx][ny] and break_grid[nx][ny] > cnt:
                    break_grid[nx][ny] = cnt
                    q.append((nx, ny, cnt))
                # is black room
                elif not grid[nx][ny] and break_grid[nx][ny] > cnt + 1:
                    break_grid[nx][ny] = cnt +1
                    q.append((nx,ny, cnt+1))
    print(break_grid[N-1][N-1])


    # break_grid = [[N*N-2 for _ in range(N)] for _ in range(N)]
    # visited = [[[False for _ in range(N)] for _ in range(N)] for _ in range(N*N)]
    # g_visited = [[False for _ in range(N)] for _ in range(N)]
    # q = deque()
    # q.append((0,0,0))
    # visited[0][0][0] = True
    # g_visited[0][0] = True
    # break_grid[0][0] = min(break_grid[0][0], 0)
    # while q:
    #     break_cnt, x, y = q.popleft()
    #     breakFlag = False
    #     for d in range(4):
    #         nx, ny = x+dx[d], y+dy[d]
    #         if inRange(nx, ny) and not g_visited[nx][ny]:
    #             if grid[nx][ny]:
    #                 if not visited[break_cnt][nx][ny]:
    #                     q.append((break_cnt, nx, ny))
    #                     visited[break_cnt][nx][ny] = True
    #                     g_visited[nx][ny] = True
    #                     break_grid[nx][ny] = min(break_grid[nx][ny], break_cnt)
    #             else:
    #                 # print(break_cnt)
    #                 if not visited[break_cnt+1][nx][ny]:
    #                     q.append((break_cnt+1, nx, ny))
    #                     visited[break_cnt+1][nx][ny] = True
    #                     g_visited[nx][ny] = True
    #                     break_grid[nx][ny] = min(break_grid[nx][ny], break_cnt+1)
    # print(break_grid[N-1][N-1])