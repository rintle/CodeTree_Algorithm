'''
2026.02월.260203.친구비.submission의 Docstring
학새잉 N명인 학교에 입학. 모든 친구와 친구
사람과 말 못함. 친구비로 친구만들예정
학생 i에게 A_i만큼 돈을 주면 1달간 친구가 되어줌.
k원의 돈이 있고, 이를 이용해 친구 사귀기 위함.
but, 친구의 친구는 친구다 라는 qudtls논리 활용
가장 적은 비용으로 모든 사람과 친구가 되는 방법 구하기
1. union-find로 친구 구하기
2. rank가 아닌, 가격으로 union 우선순위 정하기
부모가 다른 애들 찾기.
값 더해서 k랑 비교하기
'''
import sys
input = sys.stdin.readline
N, M, k = map(int, input().split())
A = [10001]+list(map(int, input().split()))
root = [i for  i in range(N+1)]

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if A[px]<A[py]:
        root[py] = px
    else:
        root[px] = py

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

minimum = set()
for i in range(1, N+1):
    minimum.add(find(i))
price = 0 
for m in minimum:
    price += A[m]
if price <= k:
    print(price)
else:
    print('Oh no')