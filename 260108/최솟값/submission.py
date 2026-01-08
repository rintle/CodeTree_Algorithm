
'''
260108.최솟값과 최댓값.submission의 Docstring
우선 내가 생각하는것이 맞는지 체크 필요.
1. List로 받기
2. 그 범위만큼 min_max 찾기
3. 값에 넣기

음 어림도 없지.
SegmentTree가 뭔지 파악하고, 진행하자.
SegmentTree란?
- 구간을 저장하기 위한 트리.
- Leaf 노드에는 원본 데이터가 들어있음.
- 각 parent node는 구간합에 대한 정보를 가지고 있다.
- Tree의 rank는 ceil(log2(N))로 정해진다.
- Tree의 크기는 2^(rank+1) 만큼 필요하다.

SegmentTree를 만드는 방법
0. 시작==끝인 경우에, 해당 노드에 값을 넣어준다. (보통 leaf 값을 넣는다)
1. 주어진 범위를 반으로 나눈다.
2. 나눠진 2개의 범위에 대해 '왼쪽 범위'를 재귀호출 한다.
3. 나눠진 2개의 범위에 대해 '오른쪽 범위'를 재귀호출 한다.
4. 현재 노드 위치에 두 범위의 합을 저장한다.
'''
from math import ceil, log2
import sys
INT_MAX = 1000000001
input = sys.stdin.readline
N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(int(input()))
# print(data)
rank = int(ceil(log2(N)))
t_size = 1<<(rank+1)
seg_tree = [0]*t_size
def makeSegTree(n, start, end):
    if start == end:
        seg_tree[n] = data[start]
        return seg_tree[n]
    mid = (start+end)//2
    left = makeSegTree(n*2, start, mid)
    right = makeSegTree(n*2+1, mid+1, end)
    seg_tree[n] = min(left, right)
    return seg_tree[n]
makeSegTree(1, 0, N-1)
# print(seg_tree)
def findMin(n, start, end, left, right):
    
    if right < start or end < left: 
        # print(f'({start}, {end}, {left, right})-return: INTMAX')
        return INT_MAX
    if left <= start and end <= right: 
        # print(f'({start}, {end}, {left, right})-return: {seg_tree}')
        return seg_tree[n]
    
    mid = (start + end)//2
    left_val = findMin(n*2, start, mid, left, right)
    right_val = findMin(n*2+1, mid+1, end, left, right)
    return min(left_val, right_val)
ans = []
for _ in range(M):
    a, b = map(int, input().split())
    ans.append(str(findMin(1, 0, N-1, a-1, b-1)))
print('\n'.join(ans))