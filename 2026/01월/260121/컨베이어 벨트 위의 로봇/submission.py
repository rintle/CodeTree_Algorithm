'''
2026.01월.260121.컨베이어 벨트 위의 로봇.submission의 Docstring
길이가 N인 컨베이어 벨트
길이가 2N인 '벨트'가 감싸고 있음

 →→→→→→→→→→→→→→→→→→→→→→→→→→
↑ 1 2 3 4 5, ....., N-1, N ↓
↑ 2N, 2N-1, ...., N+2, N+1 ↓
 ←←←←←←←←←←←←←←←←←←←←←←←←←←
1번칸이 있는 위치가 "올리는 위치"
N번칸이 있는 위치가 "내리는 위치

1. 로봇은 올리는 위치에만 올릴 수 있음
2. 로봇은 내리는 위치에 도달하면 즉시 내림
3. 로봇은 벨트 위에서 스스로 이동 할 수 있음
4. 로봇을 올리거나, 로봇이 벨트 위에서 이동하면 그 칸의 내구도는 즉시 1 감소

순서:
1. 벨트가 회전
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한칸 이동할 수 있다면 이동
  2-1. 이동 조건 : 이동 칸에 로봇이 없고, 칸의 내구도가 1 이상 남아있는 경우
3. 올리는 칸 내구도가 0이 아니면 로봇 올리기
4. 내구도 0인 칸 개수가 K개 이상이면 과정 종료. 아니면 1 돌아감
핵심: 내구도를 유지하면서 저기하기.
인덱싱 문제로, 올리는 위치: 0, 내리는 위치: N-1
벨트가 2개처럼 보이지만, 사실상 하나를 계속 이동시키는 거라고 볼 수 있음

'''
from collections import deque
N, K = map(int, input().split())
A = deque(map(int, input().split()))
robot = deque([False for _ in range(N)])
# move
def move():
    A.appendleft(A.pop())
    robot.pop()
    robot.appendleft(False)
    if robot[N-1]:
        robot[N-1] = False

def moveRobot():
    for i in range(N-1, -1, -1):
        if robot[i]:
            if not robot[i+1] and A[i+1]:
                robot[i] = False
                robot[i+1] = True
                A[i+1] = max(0, A[i+1]-1)
    if robot[N-1]:
        robot[N-1] = False

def loadRobot():
    if A[0]:
        robot[0] = True
        A[0] -= 1

def prtyPrint():
    for i in robot:
        if i:
            print('*', end='\t')
        else:
            print('-', end='\t')
    print()
    for a in range(N):
        print(A[a], end='\t')
    print()
    for a in range(2*N-1, N-1, -1):
        print(A[a], end='\t')
    print()
    print('='*30)
ans = 0
while True:
    ans+=1
    move()
    moveRobot()
    loadRobot()
    if A.count(0) >= K:
        break
print(ans)