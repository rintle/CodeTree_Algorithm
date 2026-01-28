'''
2026.01월.260128.철도공사.submission의 Docstring
2호선에서 M번의 공사를 거치려고 함.
4가지중 하나를 시행함
1. i를 가진 역의 다음 역의 번호를 출력하고, 그 사이에 j 역을 설립
2. i를 가진 역의 이전 역의 번호를 출력하고, 그 사이에 j 역을 설립
3. i를 가진 역의 다음 역을 폐쇄하고, 그 역의 고유 번호 출력
4. i를 가진 역의 이전 역을 폐쇄하고, 그 역의 고유 번호 출력

역의 개수 N, 공사 횟수 M
BN - 1
BP - 2
CN - 3
CP - 4
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
code_idx = dict()
subway = list(map(int, input().split()))
L = [-1]*1000001
R = [-1]*1000001

for i in range(N):
    L[subway[i]] = subway[i-1]
    R[subway[i]] = subway[(i+1)%N]

def pprint():
    print(L[:15])
    print(R[:15])
ans = []
for _ in range(M):
    command = input().split()
    if command[0] == 'BN':
        # i를 가진 역의 다음 역의 번호를 출력하고, 그 사이에 j 역을 설립
        i, j = map(int, command[1:])
        ans.append(str(R[i]))
        # new에 대해 저장
        L[j] = i
        R[j] = R[i]
        L[R[i]] = j
        R[i] = j
        # pprint()
    elif command[0] == 'BP':
        # i를 가진 역의 이전 역의 번호를 출력하고, 그 사이에 j 역을 설립
        i, j = map(int, command[1:])
        ans.append(str(L[i]))
        L[j] = L[i]
        R[j] = i
        R[L[i]] = j
        L[i] = j
        # pprint()
    elif command[0] == 'CN':
        i = int(command[1])
        # i를 가진 역의 다음 역을 폐쇄하고, 그 역의 고유 번호 출력
        ans.append(str(R[i]))
        close = R[i]
        R[i] = R[close]
        L[R[close]] = i
        # pprint()
    else:
        i = int(command[1])
        ans.append(str(L[i]))
        close = L[i]
        L[i] = L[close]
        R[L[close]] = i
        # pprint()
    # break
print('\n'.join(ans))