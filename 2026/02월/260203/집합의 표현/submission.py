'''
2026.02월.260203.집합의 표현.submission의 Docstring
n+1개의 집합 {0}, {1}, ..., {n}이 있음
두 원소가 같은 집합에 포함되어있는지 확인하는 연산을 수행하려 함.
합집합 연산 : 0 a b
확인 연산 : 1 a b -> a와 b가 같은 집합인지 조사
약..간 union-find로 풀면 될 것 같음.
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
root = [_ for _ in range(n+1)]
rank = [1 for _ in range(n+1)]

def find(x):    
    if root[x] == x:
        return x
    
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if rank[py]>rank[px]:
        root[px] = py
    else:
        root[py] = px
        rank[px]+=1
    
ans = []
for _ in range(m):
    c, a, b = map(int, input().split())
    if c:
        if find(a) == find(b):
            ans.append("YES")
        else:
            ans.append("NO")
    else:
        union(a, b)

print('\n'.join(ans))