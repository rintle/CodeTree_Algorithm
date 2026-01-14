'''
260114.겹치는 건 싫어.submission의 Docstring
같은 원소가 K개 이하로 들어있는 최장 연속 부분 수열의 길이 구하기.
포인터 1는 부분 수열의 시작을 나타내고,
포인터 2는 하나씩 증가하며 부분 수열을 구한다.

최장 부분 수열을 만족하지 않는 순간이 왔을 때, 만족할 때까지 포인터 1을 당긴다.
예
10 1
1 2 3 4 4 5 6 7 8 9
인 경우에는

↓
1 4 2 3 4 5 6 7 8 9
      ↑
까지 진행한 이후
↓
1 4 2 3 4 5 6 7 8 9
        ↑
일 때, 4 값이 K를 초과했으므로, 4 개수가 K보다 작아질 때 까지 포인터 1을 당긴다.
    ↓    
1 4 2 3 4 5 6 7 8 9
        ↑
당겼다면, 다시 시작한다.
'''
N, K = map(int, input().split())
a = list(map(int, input().split()))
mem = [0 for _ in range(100001)]
ans = 0
p1, p2 = 0, 0
while p2 < len(a):
    mem[a[p2]] += 1
    while mem[a[p2]] > K:
        ans = max(ans, p2-p1)
        mem[a[p1]] -= 1
        p1 += 1
    p2 += 1
else:
    ans = max(ans, p2-p1)
print(ans)