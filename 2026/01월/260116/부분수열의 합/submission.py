'''
2026.01월.260116.부분수열의 합.submission의 Docstring
N개의 정수로 이루어진 "수열"
크기가 "양수"인 부분 수열 중
수열의 원소를 다 더한 값이 S가 되는 경우의 수
'''
N, S = map(int, input().split())
data = list(map(int, input().split()))

pick = []
ans = 0
def permutation(idx):
    
    global ans
    if idx == N:
        # print(pick)
        if pick and sum(pick) == S:
            # print('add!')
            ans += 1
        return
    
    pick.append(data[idx])
    permutation(idx+1)
    pick.pop()
    permutation(idx+1)
permutation(0)
print(ans)