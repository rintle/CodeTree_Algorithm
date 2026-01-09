import heapq
N = int(input())
bag = []
for _ in range(N):
    a = list(map(int, input().split()))
    if a[0]:
        for i in range(1, len(a)):
            heapq.heappush(bag, -a[i])
    else:
        try:
            present = -heapq.heappop(bag)
            print(present)
        except:
            print(-1)