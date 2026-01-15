import heapq
N = int(input())
heaps = []
first = True
for _ in range(N):
    if first:
        for d in map(int, input().split()):
            heapq.heappush(heaps, d)
        first = False
    else:
        for d in map(int, input().split()):
            heapq.heappushpop(heaps, d)
print(heaps[0])