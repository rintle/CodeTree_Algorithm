'''
2026.01월.260128.파이제곱.submission의 Docstring
미생물이 한 마리만 남을 때까지 서로 흡수
1. 하루에 한 번 줄의 맨 앞에 있는 미생물부터 각 미생물은 차례대로 인접한 미생물
중 자신보다 크기가 작거나 같은 것들을 모두 흡수. 흡수하면 한 만큼 커짐
2. 흡수당한 미생물 사라짐. 3, 2, 1의 경우, 2는 차례가 오기 전에 흡수당해 죽음

'''
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
L = [i-1 for i in range(N)]
R = [i+1 for i in range(N)]
R[-1]=-1
alive = deque([i for i in range(N)])
while len(alive) != 1:
    left = deque()
    for cell in alive:
        if A[cell]:
            # 왼쪽 세포 냠냠
            update = A[cell]
            if L[cell] != -1 and 0<A[L[cell]]<=A[cell]:
                left_cell = L[cell]
                if left[-1] == left_cell:
                    left.pop()
                # cell 냠냠
                update += A[left_cell]
                A[left_cell] = 0
                if L[left_cell] != -1:
                    # 먹은 cell의 왼쪽의 오른쪽은 나고,
                    R[L[left_cell]] = cell
                    # 내 왼쪽은 먹은 cell의 왼쪽이다.
                    L[cell] = L[left_cell]
                else:
                    L[cell] = -1
            # 오른쪽 세포 냠냠
            if R[cell] != -1 and 0 < A[R[cell]] <= A[cell]:
                right_cell = R[cell]
                update += A[right_cell]
                A[right_cell] = 0
                if R[right_cell] != -1:
                    # 먹은 오른쪽 cell의 오른쪽의 왼쪽이 나고
                    L[R[right_cell]] = cell
                    # 내 오른쪽은 먹은 cell의 오른쪽이다
                    R[cell] = R[right_cell]
                else:
                    R[cell] = -1
            A[cell] = update
            left.append(cell)
        
    alive = left
idx = alive.pop()
print(f'{A[idx]}\n{idx+1}')

'''
  1  2  3  4  5
[-1, 0, 1, 2, 3]
[0, 1, 2, 3, 4]
[1, 2, 3, 4, -1]


4 1 3 5 2
4가 1 먹음
5 3 5 2
3은 암것도 못함
5가 3,2먹음
5 10


0  2  4  
5  5  5
'''