'''
260114.두 용액.submission의 Docstring
산성 용액과 알칼리성 용액.
산성    :  1  ~  1,000,000,000
알칼리성: -1  ~ -1,000,000,000
1. 일단 정렬한다. N은 2 이상 10000 이하니까.
2. 양 끝단에서 부터, 선택한다.
3. 두 값의 합이 0과 가까운지 확인한다 (절댓값 확인)
3. pointer를 옮기는 기준은?
3-1. 양 쪽을 미리 하나씩 옮겨보고, 둘 중 절댓값이 더 작은 쪽으로 이동한다.
 ↓
-99 -2 -1 4 98
            ↑
둘 중 누구를 옮겨야 할 지 결정해야하는데,
-99 + 4 = -95
-2 + 98 = 96 이므로, ↑를 옮기는 것이 좋다.
 ↓
-99 -2 -1 4 98
          ↑
값을 업데이트 하고, 또 비교한다.
-99 -1 = -100
-2 + 4 = 2
↓를 옮긴다. ... 이렇게 진행해보자.
'''
N = int(input())
data = sorted(map(int, input().split()))
p1, p2 = 0, N-1
ans = 2000000001
found = None
while p1 < p2:
    mix = abs(data[p1]+data[p2])
    if mix < ans:
        ans = mix
        found = (data[p1], data[p2])
    mix1 = abs(data[p1+1]+data[p2])
    mix2 = abs(data[p1]+data[p2-1])
    if mix1 < mix2:
        p1 += 1
    else:
        p2 -= 1
print(*found)