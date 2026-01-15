'''
260114.먹을 것인가 먹힐 것인가.submission의 Docstring
A, B가 주어졌을 때, 이중 루프를 돌면 되는거 아닌가?
어떤 탐색을 하는데 있어서, 정렬은 매우 중요하다.
나는 정렬을 하지 않고 진행했다 보니, 문제를 올바르게 풀지 못했다.
문제에서 정렬이 필요한 지 아닌지를 잘 판단해야할 것 같다.
'''
T = int(input())
while T:
    memory = dict()
    map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    cnt = 0
    idx = 0
    for a in A:
        while idx < len(B):
            if a > B[idx]:
                idx += 1
            else:
                break
        cnt += idx
    print(cnt)
    T -= 1