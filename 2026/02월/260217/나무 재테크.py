'''
Docstring for 2026.02월.260217.나무 재테크
NxN 크기의 땅
(r,c), 1부터 시작(노ㅑㅅ)
처음에 양분은 모든 칸에 5만큼 들어있음.

M개의 나무를 구매해 땅에 심음. 한칸에 여러개도 가능

1. 봄에 나무가 나이만큼 양분을 먹고, 나이가 1 증가.
 1-1. 여러 나무가 있다면, 어린 나무부터 양분 먹는다.
 1-2. 나이만큼 양분을 못먹으면, 즉사
2. 죽은 나무가 양분으로 변함. (죽은 나무 나이)//2

3. 5의 배수인 나이의 나무가 번식함. 인접한 8개의 칸에
   나이가 1인 나무가 생김.
4. S2D2가 땅에 양분을 추가함. A[r][c]만큼 추가함.
K년 뒤 살아있는 나무의 개수?

풀이법
최대 10x10
각 배열 위치에 나무를 priority queue로 관리하자.
spring, summer, fall, winter를 순서대로 구현해서 진행하자.
'''
from heapq import heappush, heappop, heapify
from collections import deque
import copy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
treeInfo = [[[] for _ in range(N)]for _ in range(N)]
dead = deque()
ground = [[5 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1; y -= 1
    treeInfo[x][y].append(z)

for x in range(N):
    for y in range(N):
        if treeInfo[x][y]:
            treeInfo[x][y].sort()
        treeInfo[x][y] = deque(treeInfo[x][y])
    
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

def inRange(x, y):
    return 0<=x<N and 0<=y<N

def spring_summer():    
    for x in range(N):
        for y in range(N):
            if treeInfo[x][y]:
                newTreeInfo = deque()
                dead = 0
                while treeInfo[x][y]:
                    z = treeInfo[x][y].popleft()
                    if ground[x][y] >= z:
                        ground[x][y] -= z
                        newTreeInfo.append(z+1)
                    else:
                        dead += z//2
                treeInfo[x][y] = newTreeInfo
                ground[x][y] += dead

def fall():
    for x in range(N):
        for y in range(N):
            for tree in treeInfo[x][y]:
                if tree%5==0:
                    for d in range(8):
                        nx, ny = x+dx[d], y+dy[d]
                        if inRange(nx, ny):
                            treeInfo[nx][ny].appendleft(1)
    
def winter():
    for x in range(N):
        for y in range(N):
            ground[x][y] += A[x][y]

while K:
    spring_summer()
    fall()
    winter()
    K -= 1

answer = 0
for x in range(N):
    for y in range(N):
        answer += len(treeInfo[x][y])

print(answer)