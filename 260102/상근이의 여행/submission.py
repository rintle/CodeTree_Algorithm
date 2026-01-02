'''
260102.상근이의 여행.submission의 Docstring

사이클이 생기지 않게 트리를 구성하는 문제인가?
union find로 한번 진행해보자.

'''

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

T = int(input())
while T:
    parents = [i for i in range(1001)]
    rank = [1 for _ in range(1001)]
    N, M = map(int, input().split())
    cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())
        # union
        a = find(a)
        b = find(b)
        # print('parents:',a, b)
        if a == b:
            continue
        if rank[a] < rank[b]:
            parents[a] = b
        else:
            parents[b] = a

            if rank[a] == rank[b]:
                rank[a] += 1
        cnt += 1
    print(cnt)
    T -= 1