import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap=[]
ans = []
for _ in range(N):
    c = int(input())
    if c:
        if c < 0:
            heapq.heappush(heap, (abs(c), -1))
        else:
            heapq.heappush(heap, (abs(c), 1))
    else:
        if heap:
            v = heapq.heappop(heap)
            ans.append(str(v[0]*v[1]))
        else:
            ans.append('0')
print('\n'.join(ans))