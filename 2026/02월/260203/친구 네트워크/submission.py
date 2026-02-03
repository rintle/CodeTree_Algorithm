'''
2026.02월.260203.친구 네트워크.submission의 Docstring
민혁이는 친구 만드는거 좋아함.
친구 관계가 생긴 순서대로 주어졌을 때, 몇명있는지?

이름-idx랑 매칭되는 dict가 하나 있으면 편하겠군.
'''
import sys
sys.setrecursionlimit(200000)
T = int(input())
ans = []
for _ in range(T):
    F = int(input())
    hash = dict()
    cnt = 0
    root = [i for i in range(200001)]
    friends = [1 for i in range(200001)]

    def find(x):
        if root[x] == x:
            return x
        root[x] = find(root[x])
        return root[x]
    def union(x, y):
        px = find(x)
        py = find(y)
        if px == py:
            return friends[px]
        if friends[px] > friends[py]:
            root[py] = px
            friends[px] += friends[py]
            return friends[px]
        else:
            root[px] = py
            friends[py] += friends[px]
            return friends[py]

    for __ in range(F):
        a, b= input().split()
        try:
            a = hash[a]
        except:
            hash[a] = cnt
            cnt += 1
            a = hash[a]
        try:
            b = hash[b]
        except:
            hash[b] = cnt
            cnt += 1
            b = hash[b]
        ans.append(str(union(a, b)))
print('\n'.join(ans))