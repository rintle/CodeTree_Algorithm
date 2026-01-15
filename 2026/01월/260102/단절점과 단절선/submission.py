'''
260102.단절점과 단절선.submission의 Docstring
Union Find로 하는 접근의 경우 너무 오래 걸릴 확률이 있음.

사이클이 없는 트리...
결국 리프 노드를 제거하거나 리프 노드에 연결된 에지를 제거하는 경우
단절선이나 단절점이 아니게 되는 것이다.
트리의 경우에, 어떤 에지를 자르든지 관계 없이, 무조건 yes다.
문제의 핵심은, 노드를 제거할 때, 해당 노드가 leaf 노드인지 확인하는 것 뿐이다.
'''

N = int(input())
# edges = []
degree = [0 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    degree[a] += 1
    degree[b] += 1
    # edges.append((a,b))

# edges = [(-1,-1)] + edges
ans = ''
q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 2:
        ans += 'yes\n'
    else:
        if degree[k] == 1:
            ans += 'no\n'
        else:
            ans += 'yes\n'
print(ans)