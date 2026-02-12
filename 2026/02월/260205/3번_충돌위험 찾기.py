'''
자동 운송 시스템
1. (r,c) 2차원 좌표 n개의 포인트. 1~n번호
2. 로봇별 운송 경로. m개의 포인트. 순서대로 방문
3. 로봇은 x대, 모두 0초에 출발 dxdy
4. 최단경로. 여러가지인 경우 r먼저
5. 도착하면 gone.

같은 좌표에 2대면 충돌 위험상황. 몇번 발생하는지?

시뮬레이션 문제.
1. 각 로봇은 본인 위치를 기억함
2. 그리고 grid에 위치를 업데이트함
3. 충돌여부 확인함.
'''

def solution(points, routes):
    answer = 0
    points = [[-1,-1]] + points
    m = len(routes[0])
    robots = [points[route[0]]+[0] for route in routes]
    done = [False for _ in range(len(routes))]
    # # print(robots)
    while not all(done):
        grid = [[0 for _ in range(101)] for _ in range(101)]
        for idx in range(len(robots)):
            robot = robots[idx]
            # print(robot)
            curX, curY, dst_idx = robot
            if dst_idx == m:
                done[idx] = True
                continue
            # 다음 위치로 움직이기
            dstX, dstY = points[routes[idx][dst_idx]]
            diffX = dstX-curX
            diffY = dstY-curY
            # r 먼저 움직이기
            if diffX == 0 and diffY == 0:
                nextX, nextY = curX, curY
            elif diffX != 0:
                nextX, nextY = curX+(diffX//abs(diffX)), curY
            else:
                nextX, nextY = curX, curY+(diffY//abs(diffY))
            # print(nextX, nextY)
            # 충돌 count하기
            if grid[nextX][nextY] == 1:
                answer += 1
                grid[nextX][nextY] += 1
            else:
                grid[nextX][nextY] += 1
            
            # 장소 update하기
            # 도착했다면
            if (nextX, nextY) == (dstX, dstY):
                dst_idx += 1
            robots[idx] = [nextX, nextY, dst_idx]
        # print(robots)
        # print("answer:",answer)
        # break
    
    return answer

print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [2, 4]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [4, 2], [4, 3]]))