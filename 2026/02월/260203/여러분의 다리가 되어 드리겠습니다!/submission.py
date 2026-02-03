'''
2026.02월.260203.여러분의 다리가 되어 드리겠습니다!.submission의 Docstring
선린월드에는 N개의 섬이 있다. 1, 2, ..., N
섬들은 N-1개의 다리가 잇고 있고, 왕복 가능.
(어제까지는)
다리 하나가 무너짐. 왕복불가 섬이 생김

다리를 이을 두 섬의 번호를 출력 *아무거나
역시 union-find로 부모를 정렬하고, 서로 부모가 다른 두 섬을 찾으면 될 것 같다.
'''
import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline
N = int(input())
root = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]
def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if rank[px] > rank[py]:
        root[py] = px
    elif rank[py] > rank[px]:
        root[px] = py
    else:
        root[px] = py
        rank[px] += 1

for _ in range(N-2):
    a, b = map(int, input().split())
    union(a,b)

found = False
target = find(1)
for i in range(2, N+1):
    if target != find(i):
        print(target, i)
        break