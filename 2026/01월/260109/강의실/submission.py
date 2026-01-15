'''
260109.강의실.submission의 Docstring
최소한의 강의실을 사용한다 - 최소 힙
어떻게 힙에 값을 넣을 것인가?
강의 번호는 솔직히 관련이 없다.
시작시간 == 끝시간 이어도 된다.
시작시간, 종료시간 순서대로 heap에 넣고 뽑는다?

'''
# import sys
# from heapq import heappush, heappop
# input = sys.stdin.readline
# N = int(input())
# if N == 1:
#     print(1)
# else:
#     heap = []
#     for _ in range(N):
#         i, s, e = map(int, input().split())
#         heappush(heap, (s, e))
    
#     cnt = 0
#     while heap:
#         next = []
#         prev_s, prev_e = heappop(heap)
#         for _ in range(len(heap)):
#             s, e = heappop(heap)
            
#             if prev_e <= s:
#                 prev_s, prev_e = s, e
#                 continue
#             else:
#                 heappush(next, (s, e))
#         heap = next
#         cnt += 1
#     print(cnt)
import sys
import heapq

input = sys.stdin.readline

N = int(input())
lectures = []

for _ in range(N):
    num, start, end = map(int, input().split())
    lectures.append((start, end))

# 1. 시작 시간 기준으로 정렬
lectures.sort()

# 2. 우선순위 큐 (강의실별 종료 시간을 저장)
rooms = []
# 첫 번째 강의의 종료 시간을 먼저 넣음
heapq.heappush(rooms, lectures[0][1])
for i in range(1, N):
    # 가장 빨리 끝나는 강의실의 종료 시간과 현재 강의의 시작 시간 비교
    if rooms[0] <= lectures[i][0]:
        # 기존 강의실을 이어서 쓸 수 있으므로, 기존 종료 시간 pop
        heapq.heappop(rooms)
    
    # 새로운 종료 시간을 push (기존 강의실 연장 혹은 새 강의실 추가)
    heapq.heappush(rooms, lectures[i][1])
# 큐에 남아있는 원소의 개수가 필요한 최소 강의실 개수
print(len(rooms))