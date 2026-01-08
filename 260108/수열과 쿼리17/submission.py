from math import *
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
INT_MAX = 1000000001
rank = ceil(log2(N))
t_size = 1 << (rank+1)
segTree = [0]*t_size
def makeSegTree(n, start, end):
    if start == end:
        segTree[n] = A[start]
        return segTree[n]
    mid = (start+end)//2
    segTree[n] = min(makeSegTree(n*2, start,mid), makeSegTree(n*2+1, mid+1, end))
    return segTree[n]
makeSegTree(1, 0, N-1)
def change(n, start, end, target, update):
    # 딱 그 타깃에 왔다면
    if start==end and start == target:
        segTree[n] = update
        return update
    if target < start or end < target: return segTree[n]
    mid = (start+end)//2
    segTree[n] = min(change(n*2, start, mid, target, update), change(n*2+1, mid+1, end, target, update))
    return segTree[n]

def findMin(n, start, end, left, right):
    if right < start or end < left:
        return INT_MAX
    if left <= start and end <= right:
        return segTree[n]
    mid = (start+end)//2
    return min(findMin(n*2, start, mid, left, right), findMin(n*2+1, mid+1, end, left, right))
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 1:
        change(1, 0, N-1, a-1, b)
    else:
        print(findMin(1, 0, N-1, a-1, b-1))