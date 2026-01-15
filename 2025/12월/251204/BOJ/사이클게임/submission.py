# # union find를 사용하는 문제.
# # 네놈의 뿌리가 어디냐!
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# ans = 0
# root = [i for i in range(N)]

# def find(x):
#     if root[x] == x:
#         return x
#     else:
#         root[x] = find(root[x])
#         return root[x]

# def union(x, y):
#     x = find(x)
#     y = find(y)
#     root[y] = x

# for cnt in range(M):
#     n1, n2 = map(int, input().split())
#     n1, n2 = find(n1), find(n2)

#     if n1 == n2:
#         ans = cnt+1
#         break
#     else:
#         if n1 < n2:
#             union(n1, n2)
#         else:
#             union(n2, n1)
# print(ans)

import sys
input = sys.stdin.readline
# union find를 사용하는 문제.
# 네놈의 뿌리가 어디냐!
N, M = map(int, input().split())
ans = 0
root = [i for i in range(N)]

for cnt in range(M):
    n1, n2 = map(int, input().split())
    
    parent = root[n1]
    while parent != n1:
        n1 = parent
        parent = root[n1]
    parent = root[n2]

    while parent != n2:
        n2 = parent
        parent = root[n2]
    
    if n1 == n2:
        ans = cnt+1
        break
    else:
        root[n1] = min(n1, n2)
        root[n2] = min(n1, n2)
print(ans)
