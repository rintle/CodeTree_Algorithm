'''
2026.01월.260126.ABCDE.submission의 Docstring
N명이 참가하고 있음.
0번부터 N-1번 번호.
일부 사람들은 친구.
깊이가 5번까지 내려가는 sub graph가 있는지를 물어보는 문제로 보여짐
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
adj_matrix = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_matrix[a].append(b)
    adj_matrix[b].append(a)

def dfs(no, cnt):
    global visited
    if cnt == 5:
        return True
    rlt = False
    for next in adj_matrix[no]:
        if not visited[next]:
            visited[next] = True
            rlt = dfs(next, cnt+1) or rlt
            visited[next] = False
    return rlt

flag = False
for i in range(N):
    visited[i] = True
    flag = dfs(i, 1)
    visited[i] = False
    if flag:
        break
if flag:
    print(1)
else:
    print(0)