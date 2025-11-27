"""
무조건, 첫번쨰 수 뒤에는 그 수보다 작은 수 / 그 수보다 큰 수가 존재한다.
맨 뒤에서부터 하나씩 순회하며, 크기를 비교하자.


가장 큰 수 뒤에 넣는게 이득아닌가?
나보다 작은 숫자보다는 뒤에 있으면서
그 중 가장 큰 숫자 뒤에 넣어야 한다.
**나보다 작은 수 뒤에 있는 숫자 중 가장 큰 수 뒤에 넣는다.**
나보다 바로 아래 작은 수 뒤에 있는 숫자 중 가장 큰 수 뒤에 넣는다.
무조건 나보다 바로 아래 작은 수는 존재한다.

4
2 3 1 4

4
2 1 4 3
1 4 2 3
4 1 2 3
1 2 3 4

4 
3 1 4 2
1 4 3 2 << 이따구로 넣으면 되네? 긴 하지만 4번이나 움직여야 함.
4 3 1 2
3 1 2 4
1 2 3 4

4
3 1 4 2
1 4 2 3 << 킹치만 이런 경우? 3번이면 떡을 친다.
4 1 2 3
1 2 3 4

3 1 4 2


4
3 4 2 1

5
2 5 1 4 3
5 1 4 2 3
1 4 2 3 5
4 1 2 3 5

3 2 1 5 4
2 1 5 3 4
1 5 2 3 4
5 1 2 3 4
1 2 3 4 5

나보다 작은 숫자 중 가장 큰 숫자 뒤,
그 뒤에서 가장 작은 숫자 앞

걍 닥치고 가장 큰 숫자 뒤는 아닌데...



"""


N = int(input())
nums = list(map(int, input().split()))
ans = 0
sorted_nums = sorted(nums)

def check():
    for i in range(1, N):
        if nums[i-1]+1 != nums[i]:
            return False
    return True

while True:
    first = nums[0]
    found = 101
    found_idx = 0
    for idx in range(N-1, -1, -1):
        if nums[idx] > first:
            if found > nums[idx]:
                found = nums[idx]
                found_idx = idx
            else:
                break
    if found == 101:
        found_idx = N

    for idx in range(1, found_idx):
        nums[idx-1] = nums[idx]

    nums[found_idx-1] = first
    ans += 1
    if check():
        break
print(ans)